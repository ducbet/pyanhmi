import typing

from pyanhmi.Recipe import Recipe


class Cookbook:
    RECIPES: typing.Dict[int, Recipe] = dict()

    @staticmethod
    def add_recipe(recipe):
        Cookbook.RECIPES[recipe.__hash__()] = recipe

    @staticmethod
    def has_recipe(cls):
        return Recipe.get_hash(cls) in Cookbook.RECIPES

    @staticmethod
    def get_recipe(cls):
        return Cookbook.RECIPES.get(Recipe.get_hash(cls))

    @staticmethod
    def get_all_recipes():
        return list(Cookbook.RECIPES.values())
