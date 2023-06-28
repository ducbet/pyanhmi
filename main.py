import json
from collections import defaultdict, OrderedDict
from collections.abc import Iterable

from common.schema_class import Product
from common.schema_classes_test import StrDataclass, DictsDataclass, DictClass, DictDataclass, DictsClass, \
    DefaultDictDataclass, NestedDefaultDictDataclass, DefaultDictsDataclass, CompositeClass, IntDataclass, \
    DictCompositeClass, SetClass, SetDataclass, ListDataclass, OrderedDictDataclass, TupleDataclass, TuplesDataclass, \
    FrozenSetDataclass, FrozenSetClass, FrozenSetsDataclass, UnionDataclass, UnionDataclass2, StrClass, IntClass, \
    BoolDataclass, StrictModeClass
from pyanhmi import BoolAttribute
from pyanhmi.AuthenticRecipe import AuthenticRecipe
from pyanhmi.Config import timer, Mode, Config
from pyanhmi.Cookbook import Cookbook
from pyanhmi.Error import InvalidDatatype
from pyanhmi.ObjectCreator import ObjectCreator
from pyanhmi.Recipe import Recipe


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

    data = {
        "val_1": {
            "1": {
                "val_1": "2"
            }
        }
    }
    obj = ObjectCreator.create_obj(data, DictCompositeClass)
    print(f"obj.val_1: {obj.val_1}")
    assert isinstance(obj.val_1["1"], IntClass)
    assert obj.val_1["1"].val_1 == 2

