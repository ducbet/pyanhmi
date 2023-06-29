import typing

from common.Config import Config
from common.Error import InvalidDatatype


class Recipe:
    # def __init__(self, ingredients: Dict[str, Field] = None):
    def __init__(self, ingredients=None):
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

    @staticmethod
    def get_hash(cls):
        return hash(cls)

    def __repr__(self):
        return f"Recipe(ingredients={[self.ingredients.keys()]})"

    def update(self, other: "Recipe"):
        if not isinstance(other, Recipe):
            raise InvalidDatatype(expects=Recipe, data=other)

        for other_name, other_ingredient in other.ingredients.items():
            if other_name not in self.ingredients:
                self.ingredients[other_name] = other_ingredient
                continue
            self.ingredients[other_name].update(other_ingredient)
        return self
