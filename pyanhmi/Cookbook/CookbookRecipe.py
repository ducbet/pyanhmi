import typing
from collections import defaultdict

from common.Config import Config
from pyanhmi.Cookbook.Cookbook import Cookbook
from pyanhmi.Recipe.Recipe import Recipe

T = typing.TypeVar("T")


class CookbookRecipe(Cookbook):
    # if recipe in key is None, then the recipe in value is authentic recipe
    RECIPES: typing.Dict[typing.Type[T], typing.Dict[typing.Union[str, Recipe], Recipe]] = dict()

    @staticmethod
    def add(cls: typing.Type[T], recipe: Recipe = None):
        recipies = CookbookRecipe.RECIPES.get(cls)
        if not recipies:
            from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
            authentic_recipe = AuthenticRecipe(cls=cls)
            CookbookRecipe.RECIPES[cls] = {}
            CookbookRecipe.RECIPES[cls]["AUTHENTIC_RECIPE"] = authentic_recipe

            user_defined_recipe = getattr(cls, Config.PYANHMI_RECIPE, None)
            if user_defined_recipe:
                user_defined_recipe_2 = Recipe.updated(Recipe, authentic_recipe, user_defined_recipe)
                CookbookRecipe.RECIPES[cls][user_defined_recipe] = user_defined_recipe_2

            recipies = CookbookRecipe.RECIPES.get(cls)
        if not recipe:
            return
        authentic_recipe = recipies["AUTHENTIC_RECIPE"]
        variation = Recipe.updated(Recipe, authentic_recipe, recipe)
        recipies[recipe] = variation

    @staticmethod
    def has(cls: typing.Type[T], recipe: Recipe = None) -> bool:
        """

        :param cls:
        :param recipe:
        :return:
        """
        if cls not in CookbookRecipe.RECIPES:
            return False
        if not recipe:
            # CookbookRecipe.has(cls) return True if not provide recipe
            return True
        return recipe in CookbookRecipe.RECIPES[cls]

    @staticmethod
    def get(cls: typing.Type[T], recipe: typing.Union[str, Recipe] = None) -> typing.Optional[Recipe]:
        """
        :param cls:
        :param recipe:
        :return:
        """
        if cls in CookbookRecipe.RECIPES:
            # print(f"^get. cls: {cls}, recipe: {recipe}")
            if recipe:
                return CookbookRecipe.RECIPES[cls].get(recipe)
            return CookbookRecipe.RECIPES[cls].get(getattr(cls, Config.PYANHMI_RECIPE, None)) or \
                CookbookRecipe.RECIPES[cls].get("AUTHENTIC_RECIPE")

    @staticmethod
    def clear():
        for cls, recipies in CookbookRecipe.RECIPES.items():
            recipies.clear()
        CookbookRecipe.RECIPES.clear()
