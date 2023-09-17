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
    Config.MODE = Mode.STRICT
    normalizable_fields = CookbookAttributes.get_user_defined_types(AttributeTypesChild)
    assert normalizable_fields == {AttributeTypesChild, AttributeTypesParent, CompositeClass}