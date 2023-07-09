import typing
from collections import OrderedDict

from actions.Action import Action
from common.Config import Config, EmptyValue, is_field_exist
from common.Error import InvalidDatatype
from pyanhmi.Field import Field


class Recipe:
    def __init__(self, ingredients: typing.Dict[str, Field] = None,
                 based_on_cls=None,
                 model_pre_actions: typing.List = EmptyValue.FIELD,
                 model_post_actions: typing.List = EmptyValue.FIELD,
                 fields_pre_actions: typing.List = EmptyValue.FIELD,
                 fields_post_actions: typing.List = EmptyValue.FIELD):
        self.ingredients = ingredients if ingredients else {}
        self.based_on_cls = based_on_cls
        self._model_pre_actions: list = model_pre_actions if is_field_exist(model_pre_actions) else []
        self.model_pre_actions: dict = {}
        self._model_post_actions: list = model_post_actions if is_field_exist(model_post_actions) else []
        self.model_post_actions: dict = {}

        # self._fields_pre_actions: list = fields_pre_actions
        # self.fields_pre_actions: dict = {}
        # self._fields_post_actions: list = fields_post_actions
        # self.fields_post_actions: dict = {}
        if is_field_exist(fields_pre_actions):
            for ingredient in self.ingredients.values():
                ingredient.pre_action_funcs.extend(fields_pre_actions)
                # print(f"ingredient.pre_action_funcs: {ingredient.pre_action_funcs}")
        if is_field_exist(fields_post_actions):
            for ingredient in self.ingredients.values():
                ingredient.post_action_funcs.extend(fields_post_actions)
                # print(f"ingredient.post_action_funcs: {ingredient.post_action_funcs}")

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

    @staticmethod
    def get_hash(cls):
        return hash(cls)

    def __repr__(self):
        return f"Recipe(ingredients={[self.ingredients.keys()]})"

    def update_ingredient(self, other_name, other_ingredient):
        if other_name not in self.ingredients:
            self.ingredients[other_name] = other_ingredient
            return
        self.ingredients[other_name].update(other_ingredient)

    def create_actions(self, action_funcs: list):
        actions = OrderedDict()
        for action_func in action_funcs:
            action = Action(action_func, self.based_on_cls)
            actions[action.__hash__] = action
        return actions

    def update(self, other: "Recipe"):
        if not isinstance(other, Recipe):
            raise InvalidDatatype(expects=Recipe, data=other)

        self.model_pre_actions.update(self.create_actions(self._model_pre_actions))
        self.model_pre_actions.update(self.create_actions(other._model_pre_actions))

        self.model_post_actions.update(self.create_actions(self._model_post_actions))
        self.model_post_actions.update(self.create_actions(other._model_post_actions))

        for other_name, other_ingredient in other.ingredients.items():
            self.update_ingredient(other_name, other_ingredient)
        # return self

    def execute_pre_actions(self, obj):
        for ingredient in self.ingredients.values():
            for action in ingredient.pre_actions.values():
                action.execute(obj)


    def execute_post_actions(self, obj):
        for ingredient in self.ingredients.values():
            for action in ingredient.post_actions.values():
                action.execute(obj)
