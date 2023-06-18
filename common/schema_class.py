from dataclasses import dataclass
from typing import ClassVar, Dict


@dataclass
class Product:
    id: int
    name: str
    NORMALIZE_RULES: ClassVar[dict] = {
        "id": "product_id",
        "name": "product_name",
    }

    def sample_Product_method(self):
        return


@dataclass
class ProductDescription:
    product_id: int
    description: str
    image: str = ""
    NORMALIZE_RULES: ClassVar[dict] = {
        "description": {"name": "product_description",
                        "getter_func": "normalize_description"}
    }

    # @ObjectsNormalizer.normalize_func(att_name="description")
    def normalize_description(self):
        return f"normalized {self.description}"


@dataclass
class ProductReport:
    id: int
    name: str
    description: str
    image: str = ""
    NORMALIZE_RULES: ClassVar[dict] = {
        "id": "product_id",
        "name": "product_name",
        "description": "product_description",
    }


@dataclass
class ProductDescriptionEmbedded:
    # product_id: int
    description: str
    # image: str = ""
    NORMALIZE_RULES: ClassVar[dict] = {
        "description": {"name": "product_description",
                        "getter_func": "normalize_description"}
    }

    # @ObjectsNormalizer.normalize_func(att_name="description")
    def normalize_description(self):
        return f"normalized {self.description}"


@dataclass
class ProductOuter:
    # for test embedded
    # id: int
    # name: str
    details: Dict[str, ProductDescriptionEmbedded]
    NORMALIZE_RULES: ClassVar[dict] = {
        # "id": "product_id",
        # "name": "product_name",
    }

    def sample_Product_method(self):
        return
