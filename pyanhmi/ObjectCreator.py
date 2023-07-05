import time
from collections import defaultdict
from typing import Any


from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
from common.Config import Mode, EmptyValue, is_field_exist
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from common.Error import InvalidDatatype, InvalidData
from pyanhmi.Recipe.Recipe import Recipe


class ObjectCreator:
    time_debug = defaultdict(float)

    @staticmethod
    def create_obj(obj_params: dict, obj_type: Any, recipe: Recipe = None, mode: Mode = EmptyValue.FIELD):
        if not isinstance(obj_params, dict):
            raise InvalidDatatype(msg="obj_params must be dict", expects=dict, data=obj_params)
        if not CookbookRecipe.has(obj_type):
            CookbookRecipe.add(AuthenticRecipe(cls=obj_type))

        # obj_type is cached
        recipe = recipe if recipe else CookbookRecipe.get(obj_type)
        pre_validate_params = {}
        for att_name, ingredient in recipe.ingredients.items():
            if ingredient.is_final:
                continue
            if ingredient.is_class_var:
                continue

            if att_name not in obj_params:
                if is_field_exist(ingredient.default):
                    pre_validate_params[att_name] = ingredient.default
                    continue
                raise InvalidData(f"Require {att_name} param to create {obj_type} instance")

            pre_validate_params[att_name] = ingredient.create(obj_params[att_name], mode=Mode.DUCK)
        pre_validated_obj = obj_type(**pre_validate_params)
        print()
        for att_name, validators in recipe.get_validators().items():
            for validator in validators:
                if validator.is_bound_method():
                    validator(pre_validated_obj)
                else:
                    setattr(pre_validated_obj, att_name, validator(getattr(pre_validated_obj, att_name)))

        params = {}
        for att_name, ingredient in recipe.ingredients.items():
            if ingredient.is_final:
                continue
            if ingredient.is_class_var:
                continue

            params[att_name] = ingredient.create(getattr(pre_validated_obj, att_name), mode=mode)
            # params[att_name] = ingredient.create(obj_params[att_name], mode=mode)
        validated_obj = obj_type(**params)
        return validated_obj























        # # obj_type is cached
        # recipe = recipe if recipe else CookbookRecipe.get(obj_type)
        # params = {}
        # # todo obj_params.items() -> recipe.items()
        # for param, obj_param in obj_params.items():
        #     if param not in recipe.ingredients:
        #         continue
        #     if recipe.ingredients[param].is_final:
        #         continue
        #     if recipe.ingredients[param].is_class_var:
        #         continue
        #     params[param] = recipe.ingredients[param].create(obj_param, mode=mode)
        #
        # pre_validated_obj = obj_type(**params)
        # for att_name, ingredient in recipe.ingredients.items():
        #     for validator in ingredient.validators.values():
        #         print(f"att_name: {att_name}, validator: {validator}")
        #         setattr(pre_validated_obj, att_name, validator(pre_validated_obj))
        # return pre_validated_obj
