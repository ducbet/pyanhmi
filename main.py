from common.Config import Mode, Config
from common.Error import InvalidDatatype
from common.schema_class import Product, ProductDescription
from common.schema_classes_test import UnionDataclass, CompositeClass, ListDataclass, UnionDataclass2, StrictModeClass, \
    FrozenSetDataclass, SetFieldDirectly, StrClass, IntClass, AttributeTypesChild, AttributeTypesParent
from pyanhmi import LunchBox
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create
from pyanhmi.Recipe.Recipe import Recipe

if __name__ == '__main__':
    CookbookRecipe.clear()
    product = Product(id=1, name="Pro")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")

    lunch_box = LunchBox()
    lunch_box.add(product)

    # product_rules = product.__getattribute__(Config.PYANHMI_RECIPE).ingredients
    # product_rules = CookbookRecipe.get(Product).__getattribute__(Config.PYANHMI_RECIPE).ingredients
    product_rules = CookbookRecipe.get(Product).ingredients

    assert product_rules["id"].name == "id"
    assert product_rules["id"].alias == "product_id"
    assert product_rules["id"].getter_func == "id"
    assert product_rules["name"].name == "name"
    assert product_rules["name"].alias == "product_name"
    assert product_rules["name"].getter_func == "name"
    #
    # lunch_box.add(product_description)
    # product_description_rules = product_description.__getattribute__(Config.PYANHMI_RECIPE).ingredients
    # assert product_description_rules["description"].name == "description"
    # assert product_description_rules["description"].alias == "product_description"
    # assert product_description_rules["description"].getter_func == "normalize_description"
    # assert product_description_rules["product_id"].name == "product_id"
    # assert product_description_rules["product_id"].alias == "product_id"
    # assert product_description_rules["product_id"].getter_func == "product_id"
    # assert product_description_rules["image"].name == "image"
    # assert product_description_rules["image"].alias == "image"
    #
    # assert CookbookRecipe.get(type(product)) is not None
    # assert CookbookRecipe.get(type(product_description)) is not None