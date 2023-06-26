import json
from collections import defaultdict
from collections.abc import Iterable

from common.schema_classes_test import StrDataclass, DictsDataclass, DictClass, DictDataclass, DictsClass, \
    DefaultDictDataclass, NestedDefaultDictDataclass, DefaultDictsDataclass, CompositeClass, IntDataclass
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

    try:
        # data = "123". data[0][0] will raise error
        ObjectCreator.create_obj({"val_1": "123"}, DictDataclass)
        assert False
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=f"key-value {Iterable}", data="123")