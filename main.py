import inspect

from common.schema_class import Product, ProductDescription
from common.schema_classes_test import StrClass, IntClass, ClassicParent, Level4, AttributeTypesChild, AttDict, AttAny, \
    AttFrozenSet, AttDefaultDict, AttOrderedDict, AttClassVar
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
    try:
        ObjectCreator.create_obj({}, ClassicParent)
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'parent_name'"

    try:
        ObjectCreator.create_obj({"product_name": "Pro"}, ClassicParent)
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'parent_name'"

    data = {
        "a_tuple": ("a_tuple_1", "a_tuple_2"),
        # "a_dict": {"a_dict_key": "a_dict_val"},
        "a_Optional": ({
                           "a_Optional_key_list": [
                               {
                                   "a_tuple": ("a_Optional_parent_1", "a_Optional_parent_2")
                               }
                           ],
                           "a_Optional_key_set": {1, 5, 8}
                       }, 5.2),
        # "a_Any": Level4,
        # "a_FrozenSet": {1, 5, 8},
        # "a_FrozenSet_str": {"k1": 1, "k2": 5, "k3": 8},
        # "a_attParent": {"a_tuple": ("a_attParent_1", "a_attParent_2")},
        # "a_DefaultDict": {
        #     "a_DefaultDict_key": [
        #         {"a_List": [{"a_tuple": ("a_DefaultDict_1", "a_DefaultDict_2")}]}
        #     ]
        # },
        # "a_DefaultDict_int": {
        #     "a_DefaultDict_int_key": [1, 5, 7]
        # },
        # "a_OrderedDict": {
        #     "a_OrderedDict_key_2": 1,
        #     "a_OrderedDict_key_1": 4,
        # },
        # "a_OrderedDict_list_tuple": [
        #     ("a_OrderedDict_key_2", 1),
        #     ("a_OrderedDict_key_1", 4),
        # ],
        # "a_Callable": lambda a, b: a + b,
        # "a_Final": 8866,  # should not affect final value defined in the class
        # "a_ClassVar": {"a_List": [{"a_tuple": ("a_DefaultDict_1", "a_DefaultDict_2")}]},
        # "a_ClassVar_2": 1,

    }
    obj = ObjectCreator.create_obj(data, AttributeTypesChild)
    print(obj)
    # obj = ObjectCreator.create_obj(data, AttDict)
    # obj = ObjectCreator.create_obj(data, AttAny)
    # obj = ObjectCreator.create_obj(data, AttFrozenSet)
    # obj = ObjectCreator.create_obj(data, AttDefaultDict)
    # obj = ObjectCreator.create_obj(data, AttOrderedDict)
    # obj = ObjectCreator.create_obj(data, AttClassVar)

    exit()
