import typing

from pyanhmi.Cookbook.Cookbook import Cookbook
from pyanhmi.Recipe.Recipe import Recipe


class CookbookRecipe(Cookbook):
    RECIPES: typing.Dict[int, Recipe] = dict()

    @staticmethod
    def add(recipe):
        CookbookRecipe.RECIPES[recipe.__hash__()] = recipe

    @staticmethod
    def has(recipe):
        """
        Accept both recipe or class of AuthenticRecipe
        :param recipe:
        :return:
        """
        return Recipe.get_hash(recipe) in CookbookRecipe.RECIPES

    @staticmethod
    def get(recipe):
        """
        Accept both recipe or class of AuthenticRecipe
        :param recipe:
        :return:
        """
        return CookbookRecipe.RECIPES.get(Recipe.get_hash(recipe))

    @staticmethod
    def get_all():
        return list(CookbookRecipe.RECIPES.values())
