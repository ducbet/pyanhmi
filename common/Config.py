import functools
import os
import time
from abc import ABC, abstractmethod
from enum import Enum, unique, auto



@unique
class Mode(Enum):
    DUCK = 0
    STRICT = 1
    CASTING = 2
    DUCK_TEST = 3


@unique
class EmptyValue(Enum):
    FIELD = auto()


def is_field_exist(val):
    return val is not EmptyValue.FIELD


class Config:
    PYANHMI_RECIPE = "PYANHMI_RECIPE"
    CustomAttribute = hash("CustomAttribute")

    ObjAtt_priority = 100
    OrderedDict_priority = 60
    DictAtt_priority = 50
    ListAtt_priority = 50
    SetAtt_priority = 50
    TupleAtt_priority = 50
    UnionAtt_priority = 50
    PRIMITIVE_TYPE_PRIORITY = 10
    NoneAtt_priority = 5
    AnyAtt_priority = 0

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODE = Mode.STRICT




