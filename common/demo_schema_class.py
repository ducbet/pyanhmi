from dataclasses import dataclass
from typing import ClassVar

from pyanhmi.Field import Field
from pyanhmi.Recipe.Recipe import Recipe


@dataclass
class User:
    email: str
    full_name: str
    first_name: str = ""
    last_name: str = ""
    address: str = ""

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "full_name": Field(alias="user_name"),
        }
    )

