import time
from collections import defaultdict
from typing import Any

from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
from common.Config import Mode, EmptyValue
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from common.Error import InvalidDatatype
from pyanhmi.Recipe.Recipe import Recipe


class ObjectCreator:
    time_debug = defaultdict(float)

    @staticmethod
    def create_obj(obj_params: dict, obj_type: Any, recipe: Recipe = None, mode: Mode = EmptyValue.FIELD):
        # start_time = time.perf_counter()  # 1

        if not isinstance(obj_params, dict):
            raise InvalidDatatype(msg="obj_params must be dict", expects=dict, data=obj_params)
        if not CookbookRecipe.has(obj_type):
            CookbookRecipe.add(AuthenticRecipe(cls=obj_type))

        # end_time = time.perf_counter()  # 2
        # ObjectCreator.time_debug["1"] += (end_time - start_time)  # 3

        # start_time = time.perf_counter()  # 1

        # obj_type is cached
        recipe = recipe if recipe else CookbookRecipe.get(obj_type)
        params = {}
        # todo obj_params.items() -> recipe.items()
        for param, obj_param in obj_params.items():
            start_time = time.perf_counter()  # 1

            if param not in recipe.ingredients:
                continue
            if recipe.ingredients[param].is_final:
                continue
            if recipe.ingredients[param].is_class_var:
                continue

            # end_time = time.perf_counter()  # 2
            # ObjectCreator.time_debug["1.1"] += (end_time - start_time)  # 3

            # start_time = time.perf_counter()  # 1

            params[param] = recipe.ingredients[param].create(obj_param, mode=mode)

            # end_time = time.perf_counter()  # 2
            # ObjectCreator.time_debug["1.2"] += (end_time - start_time)  # 3

        # end_time = time.perf_counter()  # 2
        # ObjectCreator.time_debug["2"] += (end_time - start_time)  # 3
        return obj_type(**params)
