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
    def create(obj_params: dict, obj_type: Any, recipe: Recipe = None, mode: Mode = EmptyValue.FIELD):
        if not isinstance(obj_params, dict):
            raise InvalidDatatype(msg="obj_params must be dict", expects=dict, data=obj_params)
        if not CookbookRecipe.has(obj_type):
            CookbookRecipe.add(AuthenticRecipe(cls=obj_type))

        recipe = recipe if recipe else CookbookRecipe.get(obj_type)
        params = {}
        for att_name, ingredient in recipe.get_ingredient_to_create_obj().items():
            if att_name not in obj_params:
                if is_field_exist(ingredient.default):
                    params[att_name] = ingredient.default
                    continue
                raise InvalidData(f"Require {att_name} param to create {obj_type} instance")

            params[att_name] = obj_params[att_name]
        obj = obj_type(**params)

        for model_pre_action in recipe.model_pre_actions.values():
            model_pre_action.execute(obj)

        for att_name in params.keys():
            ingredient = recipe.get_ingredient(att_name)
            # execute pre actions
            for pre_action in ingredient.pre_actions.values():
                pre_action.execute(obj)

            # assign evaluated value
            setattr(obj, att_name, ingredient.create(getattr(obj, att_name), mode=mode))

            # execute post actions
            for post_action in ingredient.post_actions.values():
                post_action.execute(obj)
        for model_post_action in recipe.model_post_actions.values():
            model_post_action.execute(obj)
        return obj
