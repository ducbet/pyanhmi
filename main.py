import json
from collections import defaultdict

from common.schema_classes_test import StrDataclass, DictsDataclass, DictClass, DictDataclass, DictsClass, \
    DefaultDictDataclass, NestedDefaultDictDataclass, DefaultDictsDataclass, CompositeClass
from pyanhmi.Config import timer, Mode, Config
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
    Config.MODE = Mode.DUCK
    data = {
        "val_1": {
            "1": "2"
        }
    }
    obj = ObjectCreator.create_obj(data, DefaultDictDataclass)
    obj.val_1["4"].append(5)
    obj.val_1["4"].append(6)
    print(obj.val_1)
    assert isinstance(obj.val_1, defaultdict)
    assert dict(obj.val_1) == {"1": "2", "4": [5, 6]}