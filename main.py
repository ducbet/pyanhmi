import inspect

from common.schema_class import Product, ProductDescription
from common.schema_classes_test import StrClass, IntClass, ClassicParent, Level4, AttributeTypesChild, AttDict, AttAny, \
    AttFrozenSet, AttDefaultDict, AttOrderedDict, AttClassVar, AttDictClassic
from pyanhmi import ObjectsNormalizer, StrAttribute, AnyAttribute
from pyanhmi.Config import timer, Mode, Config
from pyanhmi.Cookbook import Cookbook
from pyanhmi.ObjectCreator import ObjectCreator


# class User(BaseModel):
#     id: int
#     email: NameEmail
#     ip: IPv4Address
#     name = 'Jane Doe'

@timer
def replace_in_place():
    a = None
    for i in range(1000):
        a is None



if __name__ == '__main__':
    Config.MODE = Mode.CASTING
    print()
    print()
    print()
    print()

    data = {
        "a_dict": {"a_dict_key": "a_dict_val"},

    }
    # obj = ObjectCreator.create_obj(data, AttributeTypesChild)
    obj = ObjectCreator.create_obj(data, AttDict)
    print(f"obj: {obj.__dict__}")
    print("---")
    obj = ObjectCreator.create_obj(data, AttDictClassic)
    print(f"obj: {obj.__dict__}")
