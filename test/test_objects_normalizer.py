import json
import random
import typing
from collections import defaultdict, OrderedDict
from collections.abc import Mapping, Collection, Iterable
from datetime import datetime
from enum import Enum
from ipaddress import IPv4Address
from typing import Optional, Tuple, Dict, List, Any, Set, Union
from uuid import UUID

from _decimal import Decimal

from MostOuterSchemaclass import OuterClass
from common.NestedDirectory.NestNestedDirectory.nested_schemaclass import NestedClass
from common.schema_class import Product, ProductDescription
from common.schema_classes_test import ClassicParent, AttributeTypesChild, Level4, AttributeTypesParent, StrClass, \
    IntClass, CompositeClass, AnyDataclass, FrozenSetDataclass, OrderedDictDataclass, ClassVarDataclass, StrDataclass, \
    IntDataclass, DictsDataclass, DictDataclass, DictClass, DictsClass, DictCompositeClass, DefaultDictDataclass, \
    NestedDefaultDictDataclass, DefaultDictsDataclass, SetDataclass, SetClass, SetsDataclass, ListDataclass, \
    TupleDataclass, TuplesDataclass, FrozenSetClass, FrozenSetsDataclass, UnionDataclass, UnionDataclass2
from pyanhmi import AttributeManager, IntAttribute
from pyanhmi.Attributes.AnyAttribute import AnyAttribute
from pyanhmi.Attributes.DefaultDictAttribute import DefaultDictAttribute
from pyanhmi.Attributes.DictAttribute import DictAttribute
from pyanhmi.Attributes.ListAttribute import ListAttribute
from pyanhmi.Attributes.UnionAttribute import UnionAttribute
from pyanhmi.Config import Config, Mode
from pyanhmi.Cookbook import Cookbook
from pyanhmi.Error import InvalidDatatype, InvalidData
from pyanhmi.ObjectCreator import ObjectCreator
from pyanhmi.objects_normalizer import ObjectsNormalizer


def test_hash_Att():
    try:
        ObjectCreator.create_obj({}, AttributeTypesParent)
    except:
        pass
    try:
        ObjectCreator.create_obj({}, AttributeTypesChild)
    except:
        pass

    any_1 = AnyAttribute(int)
    any_2 = AnyAttribute(str)
    list_str = ListAttribute(List[str])
    list_int = ListAttribute(List[int])
    list_dict_1 = ListAttribute(List[Dict[str, str]])
    list_dict_2 = ListAttribute(List[Dict[str, str]])
    list_dict_3 = ListAttribute(List[Dict[str, int]])
    dict_obj_1 = DictAttribute(Dict[str, AttributeTypesParent])
    dict_obj_2 = DictAttribute(Dict[str, AttributeTypesParent])
    dict_obj_3 = DictAttribute(Dict[str, str])
    dict_obj_4 = DictAttribute(Dict[str, AttributeTypesChild])

    uniton_1 = UnionAttribute(typing.Union[typing.Tuple[str, str], typing.Tuple[int, int]])
    uniton_2 = UnionAttribute(typing.Union[typing.Tuple[int, int], typing.Tuple[str, str]])

    uniton_obj_1 = UnionAttribute(typing.Union[typing.Tuple[str, AttributeTypesParent], typing.Tuple[int, AttributeTypesChild]])
    uniton_obj_2 = UnionAttribute(typing.Union[typing.Tuple[int, AttributeTypesChild], typing.Tuple[str, AttributeTypesParent]])

    assert len({any_1, any_2}) == 1
    assert len({list_str, list_int}) == 2
    assert len({list_dict_1, list_dict_2, list_dict_3}) == 2

    s = {dict_obj_1, dict_obj_2, dict_obj_3}
    assert len(s) == 2
    assert dict_obj_1 in s or dict_obj_2 in s
    assert dict_obj_3 in s

    s = {dict_obj_1, dict_obj_4}
    assert len(s) == 2

    # assert len({uniton_1, uniton_2}) == 1  # union args order is not affected
    # assert len({uniton_obj_1, uniton_obj_2}) == 1  # union args order is not affected

    # set_atts = {uniton_obj_1, uniton_obj_2}
    # print(f"set_atts: {len(set_atts)}, {set_atts}")


def test_defaultdict_value_constructor():
    assert DefaultDictAttribute(typing.DefaultDict[str, int]).get_default_factory == int
    assert DefaultDictAttribute(typing.DefaultDict[str, float]).get_default_factory == float

    assert DefaultDictAttribute(typing.DefaultDict[str, list]).get_default_factory == list
    assert DefaultDictAttribute(typing.DefaultDict[str, list[int]]).get_default_factory == list
    assert DefaultDictAttribute(typing.DefaultDict[str, typing.List[int]]).get_default_factory == list

    assert DefaultDictAttribute(typing.DefaultDict[str, set]).get_default_factory == set
    assert DefaultDictAttribute(typing.DefaultDict[str, set[int]]).get_default_factory == set
    assert DefaultDictAttribute(typing.DefaultDict[str, typing.Set[int]]).get_default_factory == set

    assert DefaultDictAttribute(typing.DefaultDict[str, dict]).get_default_factory == dict
    assert DefaultDictAttribute(typing.DefaultDict[str, dict[str, int]]).get_default_factory == dict

    try:
        ObjectCreator.create_obj({}, AttributeTypesParent)
    except:
        pass
    assert DefaultDictAttribute(typing.DefaultDict[str, dict[str, AttributeTypesParent]]).get_default_factory == dict


def test_sort_union_args():
    try:
        ObjectCreator.create_obj({}, AttributeTypesParent)
    except:
        pass
    value_atts = UnionAttribute(Union[int, str, Any]).smart_union_value_atts
    assert len(value_atts) == 3

    value_atts = UnionAttribute(Union[int, List[str]]).smart_union_value_atts
    assert len(value_atts) == 2
    assert value_atts[0].__class__ == ListAttribute
    assert value_atts[1].__class__ == IntAttribute

    value_atts = UnionAttribute(Union[int, List[str], List[int]]).smart_union_value_atts
    assert len(value_atts) == 3
    assert value_atts[0].__class__ == ListAttribute
    assert value_atts[1].__class__ == ListAttribute
    assert value_atts[2].__class__ == IntAttribute

    value_atts = UnionAttribute(Union[List[str], int, Dict[str, int]]).smart_union_value_atts
    assert len(value_atts) == 3
    assert value_atts[-1].__class__ == IntAttribute

    value_atts = UnionAttribute(Union[List[str], int, Dict[str, AttributeTypesParent]]).smart_union_value_atts
    assert len(value_atts) == 3
    assert value_atts[0].__class__ == DictAttribute
    assert value_atts[1].__class__ == ListAttribute


def test_get_att_priority():
    try:
        ObjectCreator.create_obj({}, AttributeTypesParent)
    except:
        pass
    try:
        ObjectCreator.create_obj({}, AttributeTypesChild)
    except:
        pass
    assert AnyAttribute(str).get_att_priority() == Config.AnyAtt_priority
    assert ListAttribute(typing.List[int]).get_att_priority() == Config.ListAtt_priority
    assert DictAttribute(typing.Dict[str, AttributeTypesParent]).get_att_priority() == Config.ObjAtt_priority
    assert ListAttribute(typing.List[AttributeTypesParent]).get_att_priority() == Config.ObjAtt_priority
    assert UnionAttribute(typing.Union[typing.Dict[str, AttributeTypesParent], typing.Tuple[str, int]]).get_att_priority() == Config.ObjAtt_priority
    assert ListAttribute(typing.List[str]).get_att_priority() == Config.ListAtt_priority
    assert UnionAttribute(Optional[Tuple[Dict[str, Union[List[AttributeTypesParent], Set[int]]], Any]]).get_att_priority() == Config.ObjAtt_priority
    assert UnionAttribute(Optional[Tuple[Dict[str, Union[List[str], Set[int]]], Any]]).get_att_priority() == Config.TupleAtt_priority


def test_create_obj():
    Config.MODE = Mode.CASTING
    try:
        ObjectCreator.create_obj({}, ClassicParent)
    except InvalidDatatype as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'parent_name'"

    try:
        ObjectCreator.create_obj({"product_name": "Pro"}, ClassicParent)
    except InvalidDatatype as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'parent_name'"

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
    # obj = ObjectCreator.create_obj(data, AttributeTypesChild)
    # obj = ObjectCreator.create_obj(data, AttDict)
    # obj = ObjectCreator.create_obj(data, AttAny)
    # obj = ObjectCreator.create_obj(data, AttFrozenSet)
    # obj = ObjectCreator.create_obj(data, AttOrderedDict)
    # obj = ObjectCreator.create_obj(data, AttClassVar)
    # assert isinstance(obj.a_tuple, tuple)
    # assert isinstance(obj.a_Optional, tuple)


def test_create_str_strict():
    Config.MODE = Mode.STRICT

    obj_dataclass = ObjectCreator.create_obj({"val_1": "123"}, StrDataclass)
    obj = ObjectCreator.create_obj({"val_1": "123"}, StrClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == "123"

    try:
        ObjectCreator.create_obj({"val_1": 123}, StrDataclass)
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=123)

    try:
        ObjectCreator.create_obj({"val_1": 123}, StrClass)
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=123)


def test_create_str_casting():
    Config.MODE = Mode.CASTING

    obj_dataclass = ObjectCreator.create_obj({"val_1": "123"}, StrDataclass)
    obj = ObjectCreator.create_obj({"val_1": "123"}, StrClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == "123"

    obj_dataclass = ObjectCreator.create_obj({"val_1": 123}, StrDataclass)
    obj = ObjectCreator.create_obj({"val_1": 123}, StrClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == "123"


def test_create_int_strict():
    Config.MODE = Mode.STRICT

    obj_dataclass = ObjectCreator.create_obj({"val_1": 123}, IntDataclass)
    obj = ObjectCreator.create_obj({"val_1": 123}, IntClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == 123

    try:
        ObjectCreator.create_obj({"val_1": "123"}, IntDataclass)
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=int, data="123")

    try:
        ObjectCreator.create_obj({"val_1": "123"}, IntClass)
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=int, data="123")


def test_create_int_casting():
    Config.MODE = Mode.CASTING

    obj_dataclass = ObjectCreator.create_obj({"val_1": 123}, IntDataclass)
    obj = ObjectCreator.create_obj({"val_1": 123}, IntClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == 123

    obj_dataclass = ObjectCreator.create_obj({"val_1": "123"}, IntDataclass)
    obj = ObjectCreator.create_obj({"val_1": "123"}, IntClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj_dataclass.val_1 == 123

    try:
        ObjectCreator.create_obj({"val_1": None}, IntDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=int, data=None)

    try:
        ObjectCreator.create_obj({"val_1": "asd"}, IntDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=int, data="asd")


def test_create_obj_duck():
    Config.MODE = Mode.DUCK

    obj = ObjectCreator.create_obj({"val_1": 123.1}, StrClass)
    assert obj.val_1 == 123.1

    obj_dataclass = ObjectCreator.create_obj({"val_1": "123"}, IntDataclass)
    assert obj_dataclass.val_1 == "123"

    data = {
        "val_1": {
            "1": {
                "val_1": 2
            }
        }
    }
    obj = ObjectCreator.create_obj(data, DictCompositeClass)
    assert obj.val_1 == {
        "1": {
            "val_1": 2
        }
    }

    data = {
        "val_1": {
            "1": [2, 3.1]
        }
    }
    obj = ObjectCreator.create_obj(data, DefaultDictDataclass)
    assert isinstance(obj.val_1, dict)
    assert dict(obj.val_1) == {
        "1": [2, 3.1]
    }
    try:
        obj.val_1["4"].append(5)
        assert False
    except KeyError as e:
        assert True


def test_create_dict_strict():
    Config.MODE = Mode.STRICT

    obj_dataclass = ObjectCreator.create_obj({"val_1": {"1": 2}}, DictDataclass)
    obj = ObjectCreator.create_obj({"val_1": {"1": 2}}, DictClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == {"1": 2}

    try:
        ObjectCreator.create_obj({"val_1": {123, 123}}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=dict, data={123, 123})

    try:
        ObjectCreator.create_obj({"val_1": {123: 123}}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=123)

    try:
        ObjectCreator.create_obj({"val_1": {"123": "123"}}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=int, data="123")

    try:
        ObjectCreator.create_obj({"val_1": "123"}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=dict, data="123")

    try:
        ObjectCreator.create_obj({"val_1": ["123"]}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=dict, data=["123"])

    try:
        ObjectCreator.create_obj({"val_1": [[1, "2"], ["3", "4"]]}, DictClass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=dict, data=[[1, "2"], ["3", "4"]])

    try:
        ObjectCreator.create_obj({"val_1": [(1, "2"), ("3", "4")]}, DictClass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=dict, data=[(1, "2"), ("3", "4")])

    data = {
        "val_1": {
            "1": {
                "val_1": 2
            }
        }
    }
    obj = ObjectCreator.create_obj(data, DictCompositeClass)
    assert isinstance(obj.val_1["1"], IntClass)
    assert obj.val_1["1"].val_1 == 2

    data = {
        "val_1": {
            "1": {
                "val_1": "2"
            }
        }
    }
    try:
        ObjectCreator.create_obj(data, DictCompositeClass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=int, data="2")


def test_create_dict_casting():
    Config.MODE = Mode.CASTING

    data = {
            "val_1": [(1.1, "2")],
            "val_2": [["3", 4]],
            "val_3": {"5": "6"},
            "val_4": ["78"],
        }

    obj_dataclass = ObjectCreator.create_obj(data, DictsDataclass)
    obj = ObjectCreator.create_obj(data, DictsClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj_dataclass.val_1 == {1.1: "2"}  # val_1: dict -> no format
    assert obj_dataclass.val_2 == {"3": 4}  # val_2: Dict -> no format
    assert obj_dataclass.val_3 == {"5": 6}  # val_3: Dict[str, int]
    assert obj_dataclass.val_4 == {7: "8"}  # val_4: dict[int, str]

    obj = ObjectCreator.create_obj({"val_1": ["123"]}, DictDataclass)
    assert obj.val_1 == {"1": 2}

    obj = ObjectCreator.create_obj({"val_1": [[1, "2"], ["3", "4"]]}, DictClass)
    assert obj.val_1 == {"1": 2, "3": 4}

    obj = ObjectCreator.create_obj({"val_1": [(1, "2"), ("3", "4")]}, DictClass)
    assert obj.val_1 == {"1": 2, "3": 4}

    try:
        # data = [{1, "2"}, {"3", "4"}]. data[0][0] will raise error
        ObjectCreator.create_obj({"val_1": [{1, "2"}, {"3", "4"}]}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=f"key-value {Iterable}", data=[{1, "2"}, {"3", "4"}])

    try:
        # data = ["1", "2"]. data[0][1] will raise error
        ObjectCreator.create_obj({"val_1": ["1", "2"]}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=f"key-value {Iterable}", data=["1", "2"])

    try:
        # data = [("1")]. data[0][1] will raise error
        ObjectCreator.create_obj({"val_1": [("1")]}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=f"key-value {Iterable}", data=[("1")])

    try:
        # data = [("3", "4"), (1)]. data[1][1] will raise error
        ObjectCreator.create_obj({"val_1": [("3", "4"), (1)]}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=f"key-value {Iterable}", data=[("3", "4"), (1)])

    try:
        # data = 123. 123 is not Iterable
        ObjectCreator.create_obj({"val_1": 123}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[dict, f"key-value {Iterable}"], data=123)

    try:
        # data = "123". data[0][0] will raise error
        ObjectCreator.create_obj({"val_1": "123"}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=f"key-value {Iterable}", data="123")

    data = {
        "val_1": {
            "1": {
                "val_1": "2"
            }
        }
    }
    obj = ObjectCreator.create_obj(data, DictCompositeClass)
    assert isinstance(obj.val_1["1"], IntClass)
    assert obj.val_1["1"].val_1 == 2


def test_create_defaultdict_strict():
    Config.MODE = Mode.STRICT

    data = {
        "val_1": {
            "1": [2, 3]
        }
    }
    obj = ObjectCreator.create_obj(data, DefaultDictDataclass)
    obj.val_1["4"].append(5)
    obj.val_1["4"].append(6)
    assert isinstance(obj.val_1, defaultdict)
    assert dict(obj.val_1) == {"1": [2, 3], "4": [5, 6]}


    data = {
        "val_1": {
            "1": [2, "3"]
        }
    }
    try:
        ObjectCreator.create_obj(data, DefaultDictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=int, data="3")


    data = {
        "val_1": {
            "1": [
                {
                    "composite": "composite 1"
                },
                {
                    "composite": "composite 2"
                }
            ]
        },
        "val_2": {
            "2": [3, 4]
        }
    }
    obj = ObjectCreator.create_obj(data, DefaultDictsDataclass)
    obj.val_1["5"].append(CompositeClass("composite 3"))
    obj.val_2["6"].append(7)
    assert isinstance(obj.val_1, defaultdict)
    assert isinstance(obj.val_2, defaultdict)
    assert all(isinstance(com, CompositeClass) for com in obj.val_1["1"])
    assert {k1: [com.__dict__ for com in v1] for k1, v1 in obj.val_1.items()} == {
        "1": [
            {
                "composite": "composite 1"
            },
            {
                "composite": "composite 2"
            }
        ],
        "5": [
            {
                "composite": "composite 3"
            }
        ]
    }
    assert dict(obj.val_2) == {"2": [3, 4], "6": [7]}


def test_create_defaultdict_casting():
    Config.MODE = Mode.CASTING

    data = {
        "val_1": {
            1: [2, 3.1, "4"]
        }
    }
    obj = ObjectCreator.create_obj(data, DefaultDictDataclass)
    assert isinstance(obj.val_1, defaultdict)
    assert dict(obj.val_1) == {"1": [2, 3, 4]}

    data = {
        "val_1": {
            "1": "234"
        }
    }
    obj = ObjectCreator.create_obj(data, DefaultDictDataclass)
    obj.val_1["5"].append(6)
    obj.val_1["5"].append(7)
    assert isinstance(obj.val_1, defaultdict)
    assert dict(obj.val_1) == {"1": [2, 3, 4], "5": [6, 7]}

    data = {
        "val_1": {
            "1": {
                "2": {
                    "3": [4, 5]
                }
            }
        }
    }
    obj = ObjectCreator.create_obj(data, NestedDefaultDictDataclass)
    obj.val_1["1"]["2"]["6"].append(7)
    obj.val_1["1"]["2"]["6"].append(8)

    obj.val_1["1"]["9"]["10"].append(11)
    obj.val_1["1"]["9"]["10"].append(12)

    obj.val_1["13"]["14"]["15"].append(16)
    obj.val_1["13"]["14"]["15"].append(17)
    expect_result = {
        "1": {
            "2": {
                "3": [4, 5],
                "6": [7, 8],
            },
            "9": {
                "10": [11, 12],
            },
        },
        "13": {
            "14": {
                "15": [16, 17],
            }
        }
    }
    assert json.dumps(obj.val_1) == json.dumps(expect_result)


def test_create_ordereddict_strict():
    Config.MODE = Mode.STRICT

    data = {
        "val_1": {
            "1": 2,
            "7": 8,
        }
    }
    obj = ObjectCreator.create_obj(data, OrderedDictDataclass)
    obj.val_1["5"] = 6
    obj.val_1["3"] = 4
    assert isinstance(obj.val_1, OrderedDict)
    assert obj.val_1 == OrderedDict([("1", 2), ("7", 8), ("5", 6), ("3", 4)])


def test_create_ordereddict_casting():
    Config.MODE = Mode.CASTING

    data = {
        "val_1": {
            "1": "2",
            "7": "8",
        }
    }
    obj = ObjectCreator.create_obj(data, OrderedDictDataclass)
    assert isinstance(obj.val_1, OrderedDict)

    data = {
        "val_1": [("1", 2.1), ("7", "8")]
    }
    obj_2 = ObjectCreator.create_obj(data, OrderedDictDataclass)
    assert isinstance(obj_2.val_1, OrderedDict)
    assert obj.val_1 == obj_2.val_1

    obj.val_1["5"] = "6"
    obj.val_1["3"] = "4"
    assert obj.val_1 == OrderedDict([("1", 2), ("7", 8), ("5", "6"), ("3", "4")])


    data = {
        "val_1": [("1", 2), 123]
    }
    try:
        ObjectCreator.create_obj(data, OrderedDictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=f"key-value {Iterable}", data=[("1", 2), 123])


def test_create_set_strict():
    Config.MODE = Mode.STRICT

    obj_dataclass = ObjectCreator.create_obj({"val_1": {"1", "2"}}, SetDataclass)
    obj = ObjectCreator.create_obj({"val_1": {"1", "2"}}, SetClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert isinstance(obj.val_1, set)
    assert obj.val_1 == {"1", "2"}

    data = {
        "val_1": {1, "2"},
        "val_2": {3.1, "4"},
        "val_3": {"5", "6"},
        "val_4": {7, 8},

    }
    obj = ObjectCreator.create_obj(data, SetsDataclass)
    assert obj.val_1 == {1, "2"}
    assert obj.val_2 == {3.1, "4"}
    assert obj.val_3 == {"5", "6"}
    assert obj.val_4 == {7, 8}

    try:
        ObjectCreator.create_obj({"val_1": [1, 2]}, SetDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=set, data=[1, 2])

    try:
        ObjectCreator.create_obj({"val_1": {"1", 2}}, SetDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=2)


def test_create_set_casting():
    Config.MODE = Mode.CASTING

    obj_dataclass = ObjectCreator.create_obj({"val_1": {1, "2"}}, SetDataclass)
    obj = ObjectCreator.create_obj({"val_1": [1, 2]}, SetClass)
    obj_dict = ObjectCreator.create_obj({"val_1": {"1": 3, 2: 4}}, SetClass)
    obj_str = ObjectCreator.create_obj({"val_1": "12"}, SetClass)
    obj_range = ObjectCreator.create_obj({"val_1": range(1, 3)}, SetClass)
    obj_tuple = ObjectCreator.create_obj({"val_1": (1, 2)}, SetClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj_dataclass.__dict__ == obj_dict.__dict__
    assert obj_dataclass.__dict__ == obj_str.__dict__
    assert obj_dataclass.__dict__ == obj_range.__dict__
    assert obj_dataclass.__dict__ == obj_tuple.__dict__
    assert isinstance(obj.val_1, set)
    assert obj.val_1 == {"1", "2"}

    data = {
        "val_1": {1, "2"},
        "val_2": {3.1, "4"},
        "val_3": {5, 6},
        "val_4": {7.1, "8"},

    }
    obj = ObjectCreator.create_obj(data, SetsDataclass)
    assert obj.val_1 == {1, "2"}
    assert obj.val_2 == {3.1, "4"}
    assert obj.val_3 == {"5", "6"}
    assert obj.val_4 == {7, 8}

    try:
        ObjectCreator.create_obj({"val_1": 123}, SetDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[set, Iterable], data=123)


def test_create_frozenset_strict():
    Config.MODE = Mode.STRICT

    obj_dataclass = ObjectCreator.create_obj({"val_1": frozenset({"1", "2"})}, FrozenSetDataclass)
    obj = ObjectCreator.create_obj({"val_1": {"1", "2"}}, FrozenSetClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert not isinstance(obj.val_1, set)
    assert isinstance(obj.val_1, frozenset)
    assert obj.val_1 == frozenset({"1", "2"})

    data = {
        "val_1": {1, "2"},
        "val_2": {3.1, "4"},
        "val_3": {"5", "6"},
        "val_4": {7, 8},

    }
    obj = ObjectCreator.create_obj(data, FrozenSetsDataclass)
    assert obj.val_1 == {1, "2"}
    assert obj.val_2 == {3.1, "4"}
    assert obj.val_3 == {"5", "6"}
    assert obj.val_4 == {7, 8}

    try:
        ObjectCreator.create_obj({"val_1": [1, 2]}, FrozenSetDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[set, frozenset], data=[1, 2])

    try:
        ObjectCreator.create_obj({"val_1": {"1", 2}}, FrozenSetDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=2)


def test_create_frozenset_casting():
    Config.MODE = Mode.CASTING

    obj = ObjectCreator.create_obj({"val_1": {1, "2"}}, FrozenSetClass)
    obj_dict = ObjectCreator.create_obj({"val_1": {"1": 3, 2: 4}}, FrozenSetClass)
    obj_str = ObjectCreator.create_obj({"val_1": "12"}, FrozenSetClass)
    obj_range = ObjectCreator.create_obj({"val_1": range(1, 3)}, FrozenSetClass)
    obj_tuple = ObjectCreator.create_obj({"val_1": (1, 2)}, FrozenSetClass)
    assert obj.__dict__ == obj_dict.__dict__
    assert obj.__dict__ == obj_str.__dict__
    assert obj.__dict__ == obj_range.__dict__
    assert obj.__dict__ == obj_tuple.__dict__
    assert not isinstance(obj.val_1, set)
    assert isinstance(obj.val_1, frozenset)
    assert obj.val_1 == {"1", "2"}

    data = {
        "val_1": {1, "2"},
        "val_2": {3.1, "4"},
        "val_3": {5, 6},
        "val_4": {7.1, "8"},

    }
    obj = ObjectCreator.create_obj(data, FrozenSetsDataclass)
    assert obj.val_1 == {1, "2"}
    assert obj.val_2 == {3.1, "4"}
    assert obj.val_3 == {"5", "6"}
    assert obj.val_4 == {7, 8}

    try:
        ObjectCreator.create_obj({"val_1": 123}, FrozenSetClass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=Iterable, data=123)


def test_create_list_strict():
    Config.MODE = Mode.STRICT

    obj = ObjectCreator.create_obj({"val_1": ["1", "2"]}, ListDataclass)
    assert isinstance(obj.val_1, list)
    assert obj.val_1 == ["1", "2"]

    try:
        ObjectCreator.create_obj({"val_1": {1, 2}}, ListDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=list, data={1, 2})

    try:
        ObjectCreator.create_obj({"val_1": ["1", 2]}, ListDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=2)


def test_create_list_casting():
    Config.MODE = Mode.CASTING

    obj = ObjectCreator.create_obj({"val_1": {1, "2"}}, ListDataclass)
    obj_dict = ObjectCreator.create_obj({"val_1": {"1": 3, 2: 4}}, ListDataclass)
    obj_str = ObjectCreator.create_obj({"val_1": "12"}, ListDataclass)
    obj_range = ObjectCreator.create_obj({"val_1": range(1, 3)}, ListDataclass)
    obj_tuple = ObjectCreator.create_obj({"val_1": (1, 2)}, ListDataclass)
    assert obj.__dict__ == obj_dict.__dict__
    assert obj.__dict__ == obj_str.__dict__
    assert obj.__dict__ == obj_range.__dict__
    assert obj.__dict__ == obj_tuple.__dict__
    assert isinstance(obj.val_1, list)
    assert obj.val_1 == ["1", "2"]

    try:
        ObjectCreator.create_obj({"val_1": 123}, ListDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[list, Iterable], data=123)


def test_create_tuple_strict():
    Config.MODE = Mode.STRICT

    data = {
        "val_1": ("1", (2, "3", "4"))
    }

    obj = ObjectCreator.create_obj(data, TupleDataclass)
    assert isinstance(obj.val_1, tuple)
    assert obj.val_1 == ("1", (2, "3", "4"))

    data = {
        "val_1": ("1", [2, "3", "4"])
    }
    try:
        ObjectCreator.create_obj(data, TupleDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=tuple, data=[2, "3", "4"])


def test_create_tuple_casting():
    Config.MODE = Mode.CASTING

    data = {
        "val_1": ["1", {2: 2.1, "3": 3, "4": 4, "5": 6, "7": 8}]
    }

    obj = ObjectCreator.create_obj(data, TupleDataclass)
    assert isinstance(obj.val_1, tuple)
    assert obj.val_1 == ("1", (2, "3", "4"))

    data = {
        "val_1": ["1", "234"]
    }
    obj = ObjectCreator.create_obj(data, TupleDataclass)
    assert isinstance(obj.val_1, tuple)
    assert obj.val_1 == ("1", (2, "3", "4"))

    data = {
        "val_1": ["1", {2: 2.1, "3": 3}]
    }
    try:
        ObjectCreator.create_obj(data, TupleDataclass)
        assert False
    except InvalidData as e:
        assert e == InvalidData(msg=f"tuple expect 3 items but data has 2 items", data={2: 2.1, "3": 3})

    data = {
        "val_1": ["1", {2: 2.1, "3": 3, "4": 4, "5": 6, "7": 8}],
        "val_2": {"9", "10"},
        "val_3": [11.1, "asd"],
        "val_4": {12.1: 13, "asd": 14},
    }
    obj = ObjectCreator.create_obj(data, TuplesDataclass)
    assert isinstance(obj.val_1, tuple)
    assert obj.val_1 == ("1", (2, "3", "4"))
    assert obj.val_2 == ("9", 10) or obj.val_2 == ("10", 9)
    assert obj.val_3 == (11.1, "asd")
    assert obj.val_4 == (12.1, "asd")


def test_create_union_strict():
    Config.MODE = Mode.STRICT

    data = {
        "val_1": [
            "1", 2, {"composite": "3"}
        ]
    }

    obj = ObjectCreator.create_obj(data, UnionDataclass)
    obj_comp = obj.val_1[2]
    assert isinstance(obj_comp, CompositeClass)
    assert obj_comp.composite == "3"
    obj.val_1[2] = obj_comp.__dict__
    assert obj.val_1 == ["1", 2, {"composite": "3"}]

    obj = ObjectCreator.create_obj({"val_1": None}, UnionDataclass)
    assert obj.val_1 is None

    try:
        ObjectCreator.create_obj({"val_1": 1}, UnionDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[list, type(None)], data=1)

    try:
        ObjectCreator.create_obj({"val_1": {1, 2}}, UnionDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[list, type(None)], data={1, 2})

    try:
        ObjectCreator.create_obj({"val_1": [1.1]}, UnionDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[list, type(None)], data=[1.1])


def test_create_union_casting():
    Config.MODE = Mode.CASTING

    obj = ObjectCreator.create_obj({"val_1": {1}}, UnionDataclass)
    assert obj.val_1 == [1]

    obj = ObjectCreator.create_obj({"val_1": ("2")}, UnionDataclass)
    assert obj.val_1 == [2]

    obj = ObjectCreator.create_obj({"val_1": [3.1]}, UnionDataclass)
    assert obj.val_1 == [3]

    obj = ObjectCreator.create_obj({"val_1": [{"composite": "3"}]}, UnionDataclass)
    assert isinstance(obj.val_1[0], CompositeClass)
    assert obj.val_1[0].composite == "3"

    obj = ObjectCreator.create_obj({"val_1": None}, UnionDataclass)
    assert obj.val_1 is None

    obj = ObjectCreator.create_obj({"val_1": 1}, UnionDataclass)
    assert obj.val_1 is None  # can not cast to list -> cast to None

    data = {
        "val_1": [{1}]
    }
    obj = ObjectCreator.create_obj(data, UnionDataclass)
    assert obj.val_1 == [str({1})]  # everything can be cast to str

    try:
        ObjectCreator.create_obj({"val_1": "a"}, UnionDataclass2)
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=[int, CompositeClass], data="a")


def test_mapping_instance():
    assert isinstance(123, Iterable) is False
    assert isinstance(123.1, Iterable) is False

    assert isinstance([1, 2, 3], Iterable) is True
    assert isinstance("123", Iterable) is True
    assert isinstance([("a", 1), ("b", 2)], Iterable) is True
    assert isinstance([(1, 1), (2, 2)], Iterable) is True
    assert isinstance({"a": 1, "b": 2}, Iterable) is True


def test_create_obj_runtime_recipe():
    Config.MODE = Mode.STRICT

    data = {"id": 123}

    try:
        ObjectCreator.create_obj(data, StrClass)
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=123)

    obj_str = ObjectCreator.create_obj(data, StrClass, mode=Mode.CASTING)
    assert isinstance(obj_str.id, str)

    obj_int = ObjectCreator.create_obj(data, IntClass)
    int_recipe = getattr(IntClass, Config.PYANHMI_RECIPE)
    assert isinstance(obj_int.id, int)

    obj_str_int = ObjectCreator.create_obj(data, StrClass, int_recipe)
    assert isinstance(obj_str_int.id, int)


def test_create_sources():
    data = {
        "id": 5,
        "product_id": 5,
        "description": "Pro 5 Desc",
        "image": "",
        "name": "Pro",
    }
    objects_normalizer = ObjectsNormalizer()
    product, product_description = objects_normalizer.create_sources(data, Product, ProductDescription)

    assert product.id == 5
    assert product.name == "Pro"

    assert product_description.product_id == 5
    assert product_description.description == "Pro 5 Desc"
    assert product_description.image == ""


def test_set_normalize_rule():
    product = Product(id=1, name="Pro")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")

    objects_normalizer = ObjectsNormalizer()
    objects_normalizer.add(product)

    product_rules = product.__getattribute__(Config.PYANHMI_RECIPE).ingredients

    assert product_rules["id"].name == "id"
    assert product_rules["id"].alias == "product_id"
    assert product_rules["id"].getter_func == "id"
    assert product_rules["name"].name == "name"
    assert product_rules["name"].alias == "product_name"
    assert product_rules["name"].getter_func == "name"

    objects_normalizer.add(product_description)
    product_description_rules = product_description.__getattribute__(Config.PYANHMI_RECIPE).ingredients
    assert product_description_rules["description"].name == "description"
    assert product_description_rules["description"].alias == "product_description"
    assert product_description_rules["description"].getter_func == "normalize_description"
    assert product_description_rules["product_id"].name == "product_id"
    assert product_description_rules["product_id"].alias == "product_id"
    assert product_description_rules["product_id"].getter_func == "product_id"
    assert product_description_rules["image"].name == "image"
    assert product_description_rules["image"].alias == "image"

    assert Cookbook.RECIPES == {type(product), type(product_description)}


def test_add_source():
    product = Product(id=1, name="Pro")
    product_2 = Product(id=2, name="Pro 2")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")

    objects_normalizer = ObjectsNormalizer()
    objects_normalizer.add(product)

    assert (0, product) == objects_normalizer.sources[type(product)][0]

    objects_normalizer.add(product_2)
    assert (1, product_2) == objects_normalizer.sources[type(product_2)][1]

    objects_normalizer.add(product_description)
    assert (2, product_description) == objects_normalizer.sources[type(product_description)][0]

    objects_normalizer.add(product)
    assert (3, product) == objects_normalizer.sources[type(product)][2]

    source_count = 0
    for sources in objects_normalizer.sources.values():
        source_count += len(sources)
    assert source_count == objects_normalizer.obj_count


def test_export():
    product = Product(id=1, name="Pro")
    product_2 = Product(id=2, name="Pro 2")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")
    objects_normalizer = ObjectsNormalizer()

    objects_normalizer.add(product)
    assert objects_normalizer.export() == {
        "product_id": 1,
        "product_name": "Pro",
    }
    assert objects_normalizer.export(["product_id"]) == {
        "product_id": 1,
    }

    objects_normalizer.add(product_2)
    assert objects_normalizer.export() == {
        "product_id": 2,
        "product_name": "Pro 2",
    }

    objects_normalizer.add(product_description)
    assert objects_normalizer.export() == {
        "product_id": 5,
        "product_description": "normalized Pro 5 Desc",
        "product_name": "Pro 2",
        "image": "",
    }

    objects_normalizer.add(product)
    assert objects_normalizer.export(["product_id", "product_name"]) == {
        "product_id": 1,
        "product_name": "Pro",
    }
    assert objects_normalizer.export(["product_id", "product_description"]) == {
        "product_id": 1,
        "product_description": "normalized Pro 5 Desc",
    }
    assert objects_normalizer.export() == {
        "product_id": 1,
        "product_description": "normalized Pro 5 Desc",
        "product_name": "Pro",
        "image": "",
    }


def test_get_latest_objs():
    data = {
        "id": 5,
        "product_id": 5,
        "description": "Pro 5 Desc",
        "image": "",
        "name": "Pro",
    }
    objects_normalizer = ObjectsNormalizer(data, Product, ProductDescription)
    product = objects_normalizer.get_latest_objs(Product)
    assert product is ObjectsNormalizer.get_real_obj(objects_normalizer.sources[Product][-1])

    product, product_description = objects_normalizer.get_latest_objs(Product, ProductDescription)

    assert product is ObjectsNormalizer.get_real_obj(objects_normalizer.sources[Product][-1])
    assert product_description is ObjectsNormalizer.get_real_obj(objects_normalizer.sources[ProductDescription][-1])

    try:
        objects_normalizer.get_latest_objs(ClassicParent)
    except IndexError as e:
        assert "list index out of range" in str(e)
    try:
        objects_normalizer.get_latest_objs(None)
    except IndexError as e:
        assert "list index out of range" in str(e)
    try:
        objects_normalizer.get_latest_objs(Product, None)
    except IndexError as e:
        assert "list index out of range" in str(e)
    try:
        objects_normalizer.get_latest_objs(Product, ClassicParent)
    except IndexError as e:
        assert "list index out of range" in str(e)


def test_get_all_objs():
    product = Product(id=1, name="Pro")
    product_2 = Product(id=2, name="Pro 2")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")
    objects_normalizer = ObjectsNormalizer()

    objects_normalizer.add(product)
    assert objects_normalizer.get_all_objs() == [product]

    objects_normalizer.add(product_description)
    assert objects_normalizer.get_all_objs() == [product, product_description]

    objects_normalizer.add(product_2)
    assert objects_normalizer.get_all_objs() == [product, product_description, product_2]

    objects_normalizer.add(product_description)
    assert objects_normalizer.get_all_objs() == [product, product_description, product_2, product_description]

    objs = [product, product_2, product_description]
    rand_total = 10
    rand_result = []
    for _ in range(rand_total):
        rand_obj = random.choice(objs)
        objects_normalizer.add(rand_obj)
        rand_result.append(rand_obj)

    assert objects_normalizer.get_all_objs() == [product, product_description, product_2, product_description] + rand_result


def test_get_normalizable_fields():
    normalizable_fields = AttributeManager.get_user_defined_types(AttributeTypesChild)
    assert normalizable_fields == {AttributeTypesChild, AttributeTypesParent, CompositeClass}


def test_is_normalizable_fields():
    checks = {
        OuterClass: True,
        NestedClass: True,
        AttributeTypesChild: True,
        Any: False,
        Dict: False,
        Union: False,
        Decimal: False,
        Enum: False,
        IPv4Address: False,
        UUID: False,
        datetime: False,
        defaultdict: False,
        frozenset: False,
        int: False,
        float: False,
        list: False,
    }
    for cls, is_normalizable_field in checks.items():
        # print(f"normalizable: {TypeCheckManager.is_normalizable_fields(cls)}, {cls}, __module__: {cls.__module__}")
        assert AttributeManager.is_user_defined_type(cls) == is_normalizable_field
