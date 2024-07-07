from dataclasses import dataclass
from typing import ClassVar, Dict, List

from pydantic import BaseModel

from pyanhmi.Field import Field
from pyanhmi.Recipe.Recipe import Recipe


@dataclass
class Product:
    id: int
    name: str

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "id": Field(alias="product_id"),
            "name": Field(alias="product_name"),
        }
    )

    def sample_Product_method(self):
        return


@dataclass
class ProductDescription:
    product_id: int
    description: str
    image: str = ""

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "description": Field(alias="product_description", getter_func="upper"),
        }
    )

    # @ObjectsNormalizer.normalize_func(att_name="description")  # todo
    def upper(self):
        return (self.description or "").upper()


@dataclass
class Product2:
    id: int
    name: str = "sample name"
    description: str = "sample des"

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "id": Field(alias="product_id"),
            "name": Field(alias="product_name"),
            "description": Field(alias="product_description"),
        }
    )


@dataclass
class ConvertedProduct:
    id: int
    name: str
    description: str
    image: str
    price: int = 250000

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "id": Field(alias="product_id"),
            "name": Field(alias="product_name"),
            "description": Field(alias="product_description"),
        }
    )


@dataclass
class ProductDescriptionEmbedded:
    # product_id: int
    description: str
    # image: str = ""

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "description": Field(alias="product_description", getter_func="normalize_description"),
        }
    )

    # @ObjectsNormalizer.normalize_func(att_name="description")
    def normalize_description(self):
        return f"normalized {self.description}"


@dataclass
class ProductOuter:
    id: int
    name: str
    details: Dict[str, ProductDescriptionEmbedded]

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "id": Field(alias="product_id"),
            "name": Field(alias="product_name"),
        }
    )

    def sample_Product_method(self):
        return


@dataclass
class PublicApiEntry:
    API: str
    Description: str
    Auth: str
    HTTPS: bool
    Cors: str
    Link: str
    Category: str


@dataclass
class PublicApi:
    count: int
    entries: List[PublicApiEntry]


class PydanticPublicApiEntry(BaseModel):
    API: str
    Description: str
    Auth: str
    HTTPS: bool
    Cors: str
    Link: str
    Category: str


class PydanticPublicApi(BaseModel):
    count: int
    entries: List[PydanticPublicApiEntry]
