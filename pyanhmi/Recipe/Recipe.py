import typing
from collections import OrderedDict

from actions.Action import Action
from common.Config import Config, EmptyValue, is_field_exist
from common.Error import InvalidDatatype
from pyanhmi.Field import Field


class Recipe:
    def __init__(self, ingredients: typing.Dict[str, Field] = None,
                 based_on_cls=None,
                 model_pre_actions: typing.List = None,
                 model_post_actions: typing.List = None,
                 fields_pre_actions: typing.List = None,
                 fields_post_actions: typing.List = None):
        self.ingredients = ingredients if ingredients else {}
        self.model_pre_action_funcs: list = model_pre_actions if model_pre_actions else []
        self.model_pre_actions = []
        self.model_post_action_funcs: list = model_post_actions if model_post_actions else []
        self.model_post_actions = []

        if fields_pre_actions:
            for ingredient in self.ingredients.values():
                ingredient.pre_action_funcs.extend(fields_pre_actions)
                # print(f"ingredient.pre_action_funcs: {ingredient.pre_action_funcs}")
        if fields_post_actions:
            for ingredient in self.ingredients.values():
                ingredient.post_action_funcs.extend(fields_post_actions)
                # print(f"ingredient.post_action_funcs: {ingredient.post_action_funcs}")
        self.based_on_cls = based_on_cls

    @staticmethod
    def get_instance_attributes(obj) -> typing.Set[str]:
        return set([attr for attr in obj.__dir__()
                    if attr != Config.PYANHMI_RECIPE and
                    not attr.startswith("_") and
                    not hasattr(obj.__getattribute__(attr), "__call__")])

    def get_ingredient(self, name: str):
        return self.ingredients.get(name)

    def add_ingredient(self, name: str, field):
        self.ingredients[name] = field

    def get_ingredient_to_create_obj(self):
        return {att_name: ingredient for att_name, ingredient in self.ingredients.items()
                if not ingredient.is_final and not ingredient.is_class_var}

    # @staticmethod
    # def get_hash(cls):
    #     return hash(cls)

    def __repr__(self):
        return f"Recipe(ingredients={list(self.ingredients.keys())})"

    def execute_pre_actions(self, obj):
        for ingredient in self.ingredients.values():
            for action in ingredient.pre_actions.values():
                action.execute(obj)

    def execute_post_actions(self, obj):
        for ingredient in self.ingredients.values():
            for action in ingredient.post_actions.values():
                action.execute(obj)

    @staticmethod
    def updated(cls, recipe_1: "Recipe", recipe_2: "Recipe"):
        # recipe_1 should be AuthenticRecipe, recipe_2 should be user-defined Recipe
        def create_actions(action_funcs: list):
            # actions = {}
            # for action_func in action_funcs:
            #     action = Action(action_func, based_on_cls)
            #     actions[action.__hash__] = action
            # return actions
            return [Action(action_func, new_recipe.based_on_cls) for action_func in action_funcs]

        new_recipe = cls()
        # new_recipe.ingredients = recipe_1.ingredients
        new_recipe.based_on_cls = recipe_1.based_on_cls or recipe_2.based_on_cls

        new_recipe.model_pre_action_funcs.extend(recipe_1.model_pre_action_funcs)
        new_recipe.model_pre_action_funcs.extend(recipe_2.model_pre_action_funcs)
        new_recipe.model_pre_actions = create_actions(new_recipe.model_pre_action_funcs)

        new_recipe.model_post_action_funcs.extend(recipe_1.model_post_action_funcs)
        new_recipe.model_post_action_funcs.extend(recipe_2.model_post_action_funcs)
        new_recipe.model_post_actions = create_actions(new_recipe.model_post_action_funcs)

        for field_name in list(recipe_1.ingredients.keys()) + list(recipe_2.ingredients.keys()):
            # do not use set(list(recipe_1.ingredients.keys()) + list(recipe_2.ingredients.keys())) to manage the order of fields
            if field_name not in recipe_1.ingredients:
                new_recipe.ingredients[field_name] = Field.copy(Field, recipe_2.ingredients[field_name])
                continue
            if field_name not in recipe_2.ingredients:
                new_recipe.ingredients[field_name] = Field.copy(Field, recipe_1.ingredients[field_name])
                continue
            new_recipe.ingredients[field_name] = Field.updated(Field,
                                                               recipe_1.ingredients[field_name],
                                                               recipe_2.ingredients[field_name])
            new_recipe.ingredients[field_name].pre_actions = create_actions(new_recipe.ingredients[field_name].pre_action_funcs)
            new_recipe.ingredients[field_name].post_actions = create_actions(new_recipe.ingredients[field_name].post_action_funcs)