from typing import Optional, Any

from common.Config import Config, Mode
from common.Error import InvalidDatatype
from common.schema_class import Product, ProductDescription
from common.schema_classes_test import ClassicParent, SetFieldDirectly
from pyanhmi import LunchBox
from pyanhmi.Creator import _create, bulk_create

if __name__ == '__main__':
    print(SetFieldDirectly.bounded_action_1)
    print(type(SetFieldDirectly.bounded_action_1))