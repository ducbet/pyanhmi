import json
from collections import defaultdict, OrderedDict
from collections.abc import Iterable

from common.schema_classes_test import StrDataclass, DictsDataclass, DictClass, DictDataclass, DictsClass, \
    DefaultDictDataclass, NestedDefaultDictDataclass, DefaultDictsDataclass, CompositeClass, IntDataclass, \
    DictCompositeClass, SetClass, SetDataclass, ListDataclass, OrderedDictDataclass, TupleDataclass, TuplesDataclass, \
    FrozenSetDataclass, FrozenSetClass, FrozenSetsDataclass, UnionDataclass, UnionDataclass2, StrClass, IntClass
from pyanhmi import BoolAttribute
from pyanhmi.Config import timer, Mode, Config
from pyanhmi.Error import InvalidDatatype
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
    Config.MODE = Mode.STRICT

    print(BoolAttribute.cast_to_bool(12))






