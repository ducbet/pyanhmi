from typing import Any

from pyanhmi.Config import Config
from pyanhmi.Cookbook import Cookbook
from pyanhmi.Recipe import Recipe


class ObjectCreator:
    @staticmethod
    def _try_create_obj(obj_type, obj_params: dict = None):
        """
        There are two solutions:
        1. Call obj_type() and retrieving all required arguments
            - Can initialize mock instance (no params required)
            - Optional arguments can be ignored
        2. Call obj_type with all possible arguments and removing redundant arguments until can init instance successful
        :param obj_type:
        :param obj_params: Use solution 1 if None else solution 2
        :return:
        """
        if not obj_params:
            obj = Cookbook.try_mock_obj(obj_type)
            return obj
        for num_try in range(len(obj_params)):
            try:
                return obj_type(**obj_params)
            except TypeError as e:
                # redundant_key will raise error: __init__() got an unexpected keyword argument 'redundant_key'
                # -> remove redundant_key from obj_params until success
                err_msg = str(e)
                if "__init__() got an unexpected keyword argument " not in err_msg:
                    raise e
                redundant_key = err_msg \
                    .replace("__init__() got an unexpected keyword argument ", "") \
                    .replace("'", "")
                obj_params = {k: v for k, v in obj_params.items() if k != redundant_key}
        return obj_type()  # will raise error: TypeError: __init__() missing 1 required positional argument...

    @staticmethod
    def create_obj(obj_params: dict, obj_type: Any, recipe: Recipe = None):
        # print(f"create_obj: obj_type: {obj_type}, {obj_params}")
        if not Cookbook.is_recipe_completed(obj_type):
            Cookbook.create_recipe(cls=obj_type)

        # obj_type is cached
        recipe = recipe if recipe else getattr(obj_type, Config.PYANHMI_RECIPE)
        params = {}
        for param, obj_param in obj_params.items():
            if param not in recipe.ingredients:
                continue
            if recipe.ingredients[param].is_final:
                continue
            if recipe.ingredients[param].is_class_var:
                continue
            params[param] = recipe.ingredients[param].create(obj_param)
        return obj_type(**params)
