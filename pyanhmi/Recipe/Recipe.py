import typing

from common.Config import Config, EmptyValue
from common.Error import InvalidDatatype
from pyanhmi.Field import Field


class Recipe:
    def __init__(self, ingredients: typing.Dict[str, Field] = None):
        # todo how to add Dict[str, Field]?
        self.ingredients = ingredients if ingredients else {}

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

    def update(self, other: "Recipe"):
        if not isinstance(other, Recipe):
            raise InvalidDatatype(expects=Recipe, data=other)

        for other_name, other_ingredient in other.ingredients.items():
            self.update_ingredient(other_name, other_ingredient)
        return self

    def get_pre_actions(self) -> dict:
        return {att_name: ingredient.pre_actions.values()
                for att_name, ingredient in self.ingredients.items()}

    def execute_pre_actions(self, obj):
        for ingredient in self.ingredients.values():
            for action in ingredient.pre_actions.values():
                action.execute(obj)

    def get_post_actions(self) -> dict:
        return {att_name: ingredient.post_actions.values()
                for att_name, ingredient in self.ingredients.items()}

    def execute_post_actions(self, obj):
        for ingredient in self.ingredients.values():
            for action in ingredient.post_actions.values():
                action.execute(obj)
