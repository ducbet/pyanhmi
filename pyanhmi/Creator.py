from typing import Any, Optional, List, Union, Tuple, TypeVar, overload, Type

from common.Config import Mode, EmptyValue, is_field_exist, Config
from common.Error import InvalidDatatype, InvalidData
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
from pyanhmi.Recipe.Recipe import Recipe

T = TypeVar("T")


def _create(data: dict, cls: Type[T], recipe: Recipe = None, mode: Mode = None) -> T:
    """

    :param data:
    :param cls:
    :param recipe:
    :param mode:
    :return:
    """
    if not isinstance(data, dict):
        raise InvalidDatatype(msg="data must be dict", expects=dict, data=data)

    recipe = recipe if recipe else CookbookRecipe.get(cls, recipe)
    init_params = {}
    # print(f"_create. CookbookRecipe: {CookbookRecipe.RECIPES}")
    # print(f"_create. recipe: {recipe}")
    for att_name, ingredient in recipe.get_ingredient_to_create_obj().items():
        if att_name not in data:
            if is_field_exist(ingredient.default):
                init_params[att_name] = ingredient.default
                continue
            raise InvalidData(f"Require {att_name} param to create {cls} instance")

        init_params[att_name] = data[att_name]
    obj = cls(**init_params)
    for model_pre_action in recipe.model_pre_actions:
        model_pre_action.execute(obj)

    for att_name in init_params.keys():
        ingredient = recipe.get_ingredient(att_name)
        # execute pre actions
        for pre_action in ingredient.pre_actions:
            pre_action.execute(obj)
        # assign evaluated value
        setattr(obj, att_name, ingredient.create(getattr(obj, att_name), mode=mode))

        # execute post actions
        for post_action in ingredient.post_actions:
            post_action.execute(obj)
    for model_post_action in recipe.model_post_actions:
        model_post_action.execute(obj)
    return obj


@overload
def create(data: dict, classes: Type[T], recipes: Recipe = None, mode: Mode = None) -> T: ...


@overload
def create(data: dict, classes: List[Type], recipes: List[Recipe] = None, mode: Mode = None) -> tuple: ...


def create(data: dict,
           classes: Union[Type[T], List[Type]],
           recipes: Optional[Union[Recipe, List[Recipe]]] = None,
           mode: Mode = None) -> Union[T, tuple]:
    """

    :param data:
    :param classes:
    :param recipes:
    :param mode:
    :return:
    """
    if not data or not classes:
        # must have both data and classes
        return tuple()

    if isinstance(classes, list):
        if not isinstance(recipes, list):
            recipes = [recipes] * len(classes)
        result = []
        for idx, cls in enumerate(classes):
            recipe = recipes[idx] or getattr(cls, Config.PYANHMI_RECIPE, None)
            if not CookbookRecipe.has(cls, recipe):
                CookbookRecipe.add(cls=cls, recipe=recipe)
            result.append(_create(data, cls, recipe, mode))
        return tuple(result)

    recipe = recipes or getattr(classes, Config.PYANHMI_RECIPE, None)
    if not CookbookRecipe.has(classes, recipe):
        CookbookRecipe.add(cls=classes, recipe=recipe)
    return _create(data, classes, recipe, mode)
