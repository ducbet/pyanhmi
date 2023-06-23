from dataclasses import dataclass, field
from typing import Dict

from pyanhmi.Field import Field


@dataclass
class Recipe:
    is_completed: bool = False
    ingredients: Dict[str, Field] = field(default_factory=dict)

    def get_ingredient(self, name: str):
        return self.ingredients.get(name)

    def add_ingredient(self, name: str, field):
        self.ingredients[name] = field
