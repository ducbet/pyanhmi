from typing import Any

from pyanhmi.AuthenticRecipe import AuthenticRecipe
from pyanhmi.Config import Config, Mode
from pyanhmi.Cookbook import Cookbook
from pyanhmi.Error import InvalidDatatype
from pyanhmi.Recipe import Recipe


class ObjectCreator:

    @staticmethod
    def create_obj(obj_params: dict, obj_type: Any, recipe: Recipe = None, mode: Mode = None):
        if not isinstance(obj_params, dict):
            raise InvalidDatatype(msg="obj_params must be dict", expects=dict, data=obj_params)
        if not Cookbook.has_recipe(obj_type):
            Cookbook.add_recipe(AuthenticRecipe(cls=obj_type))

        # obj_type is cached
        recipe = recipe if recipe else Cookbook.get_recipe(obj_type)
        params = {}
        # print(recipe)
        # print(recipe.get_ingredient("val_1"))
        for param, obj_param in obj_params.items():
            if param not in recipe.ingredients:
                continue
            if recipe.ingredients[param].is_final:
                continue
            if recipe.ingredients[param].is_class_var:
                continue
            params[param] = recipe.ingredients[param].create(obj_param, mode=mode)
        return obj_type(**params)
