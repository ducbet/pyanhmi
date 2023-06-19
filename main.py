import typing
from collections import OrderedDict

from common.schema_classes_test import Level4, AttributeTypesChild, AttributeTypesComposite
from objects_normalizer.CacheRule import CacheRule
from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.DefaultDictTypeAttribute import DefaultDictTypeAttribute
from objects_normalizer.ObjectCreator import ObjectCreator

if __name__ == '__main__':

    # exit()
    # mysql_client = MysqlClient()

    data = {
        "a_tuple": ("a_tuple_1", "a_tuple_2"),
        "a_dict": {"a_dict_key": "a_dict_val"},
        "a_Optional": ({
                           "a_Optional_key_list": [
                               {
                                   "a_tuple": ("a_Optional_parent_1", "a_Optional_parent_2")
                               }
                           ],
                           "a_Optional_key_set": {1, 5, 8}
                       }, 5.2),
        "a_Any": Level4,
        "a_FrozenSet": {1, 5, 8},
        "a_FrozenSet_str": {"k1": 1, "k2": 5, "k3": 8},
        "a_attParent": {"a_tuple": ("a_attParent_1", "a_attParent_2")},
        "a_DefaultDict": {
            "a_DefaultDict_key": [
                {"a_List": [{"a_tuple": ("a_DefaultDict_1", "a_DefaultDict_2")}]}
            ]
        },
        "a_DefaultDict_int": {
            "a_DefaultDict_int_key": [1, 5, 7]
        },
        "a_OrderedDict": {
            "a_OrderedDict_key_2": 1,
            "a_OrderedDict_key_1": 4,
        },
        "a_OrderedDict_list_tuple": [
            ("a_OrderedDict_key_2", 1),
            ("a_OrderedDict_key_1", 4),
        ],
        "a_Callable": lambda a, b: a + b,
        "a_Final": 8866,  # should not affect final value defined in the class
        "a_ClassVar": {"a_List": [{"a_tuple": ("a_DefaultDict_1", "a_DefaultDict_2")}]},
        "a_ClassVar_2": 1,

    }
    print()
    tmp = ObjectCreator.create_obj(data, AttributeTypesChild)
    print()
    rules = getattr(AttributeTypesChild, Config.normalize_rules_field_name_2)
    # for rule in rules.values():
    #     print(f"rule: {rule}")
    print()
    print(tmp)
    print()
    print()

