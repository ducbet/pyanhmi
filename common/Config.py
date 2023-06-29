import functools
import os
import time
from abc import ABC, abstractmethod
from enum import Enum, unique


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        ms = run_time * 1000
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs, {ms:.1f}: ms")
        return value
    return wrapper_timer


@unique
class Mode(Enum):
    DUCK = 0
    STRICT = 1
    CASTING = 2


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




