from typing import Any, Optional, List, Union, Tuple, TypeVar, overload

from common.Config import Mode, EmptyValue, is_field_exist
from common.Error import InvalidDatatype, InvalidData
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
from pyanhmi.Recipe.Recipe import Recipe

T = TypeVar("T")


def _create(data: dict, cls: T, recipe: Recipe = None, mode: Mode = None) -> T:
    """

    :param data:
    :param cls:
    :param recipe:
    :param mode:
    :return:
    """
    if not isinstance(data, dict):
        raise InvalidDatatype(msg="data must be dict", expects=dict, data=data)

    recipe = recipe if recipe else CookbookRecipe.get(cls)
    init_params = {}
    # print(f"_create. recipe: {recipe.get_ingredient('val_1')}")
    for att_name, ingredient in recipe.get_ingredient_to_create_obj().items():
        if att_name not in data:
            if is_field_exist(ingredient.default):
                init_params[att_name] = ingredient.default
                continue
            raise InvalidData(f"Require {att_name} param to create {cls} instance")

        init_params[att_name] = data[att_name]
    obj = cls(**init_params)
    for model_pre_action in recipe.model_pre_actions.values():
        model_pre_action.execute(obj)

    for att_name in init_params.keys():
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


@overload
def create(data: dict, classes: T, recipes: Recipe = None, mode: Mode = None) -> T: ...


@overload
def create(data: dict, classes: List[T], recipes: List[Recipe] = None, mode: Mode = None) -> Tuple[T]: ...


def create(data: dict,
           classes: Union[T, List[T]],
           recipes: Optional[Union[Recipe, List[Recipe]]] = None,
           mode: Mode = None) -> Union[Tuple[T], T]:
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

    if not isinstance(classes, list):
        if not CookbookRecipe.has(classes):
            # if cls is not cached in CookbookRecipe, then cache before creating
            # nested classes are also cached
            CookbookRecipe.add(AuthenticRecipe(cls=classes))
        return _create(data, classes, recipes, mode)

    # classes is list
    for cls in classes:
        if not CookbookRecipe.has(cls):
            CookbookRecipe.add(AuthenticRecipe(cls=cls))
    if not recipes:
        return tuple([_create(data, cls, None, mode) for cls in classes])
    if len(classes) != len(recipes):
        # if there are recipes, then the length of recipes must be matched with classes
        raise ValueError(f"len(classes) != len(recipes). "
                         f"len(classes) == {len(classes)}, "
                         f"len(recipes) == {len(recipes)}")
    return tuple([_create(data, cls, recipes[idx], mode) for idx, cls in enumerate(classes)])
