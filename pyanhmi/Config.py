import functools
import os
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


class Config:
    PYANHMI_RECIPE = "PYANHMI_RECIPE"

    ObjAtt_priority = 100
    OrderedDict_priority = 60
    DictAtt_priority = 50
    ListAtt_priority = 50
    SetAtt_priority = 50
    TupleAtt_priority = 50
    UnionAtt_priority = 50
    PRIMITIVE_TYPE_PRIORITY = 10
    AnyAtt_priority = 0

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DISCRIMINATE_PRIMITIVE_TYPES = True



