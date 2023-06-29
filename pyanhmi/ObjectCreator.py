from typing import Any

from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
from common.Config import Mode
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from common.Error import InvalidDatatype
from pyanhmi.Recipe.Recipe import Recipe


class ObjectCreator:

    @staticmethod
    def create_obj(obj_params: dict, obj_type: Any, recipe: Recipe = None, mode: Mode = None):
        if not isinstance(obj_params, dict):
            raise InvalidDatatype(msg="obj_params must be dict", expects=dict, data=obj_params)
        if not CookbookRecipe.has(obj_type):
            CookbookRecipe.add(AuthenticRecipe(cls=obj_type))

        # obj_type is cached
        recipe = recipe if recipe else CookbookRecipe.get(obj_type)
        params = {}
        for param, obj_param in recipe.ingredients.items():
            if param not in recipe.ingredients:
                continue
            if recipe.ingredients[param].is_final:
                continue
            if recipe.ingredients[param].is_class_var:
                continue
            params[param] = recipe.ingredients[param].create(obj_param, mode=mode)
        return obj_type(**params)
