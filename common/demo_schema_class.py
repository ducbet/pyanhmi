from dataclasses import dataclass
from typing import ClassVar

from pyanhmi.Field import Field
from pyanhmi.Recipe.Recipe import Recipe


@dataclass
class UserDb1:
    email: str
    name: str
    address: str = ""

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "email": Field(alias="user_email"),
            "name": Field(alias="user_name"),
        }
    )


@dataclass
class UserDb2:
    user_email: str
    full_name: str
    first_name: str = ""
    last_name: str = ""

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "full_name": Field(alias="user_name"),
        }
    )


@dataclass
class ReportUser:
    mail: str
    name: str
    first_name: str
    last_name: str
    address: str

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "mail": Field(alias="user_email"),
            "name": Field(alias="user_name"),
        }
    )

