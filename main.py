import json
from collections import defaultdict
from collections.abc import Iterable

from common.schema_classes_test import StrDataclass, DictsDataclass, DictClass, DictDataclass, DictsClass, \
    DefaultDictDataclass, NestedDefaultDictDataclass, DefaultDictsDataclass, CompositeClass, IntDataclass, \
    DictCompositeClass
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
    Config.MODE = Mode.CASTING

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