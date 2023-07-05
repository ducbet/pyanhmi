from common.Config import EmptyValue, is_field_exist
from common.Error import ValidatorMissing


class Validator:
    def __init__(self, func, based_on_cls):
        """
        If func is string -> belongs to based_on_cls
        If func is function -> 2 possibilities
        1. If can not find func's name in cls -> unbounded function. getattr(based_on_cls, func.__name__, None) == None
        2. If can find func's name in cls:
            2.1. Just because the same name -> check whether have "." in __qualname__
                2.1.1. If there is "." in __qualname__ -> belong to some class or nested function -> to check... todo
                2.1.2. If there is not "." in __qualname__ -> unbounded function
            2.2. Is method of based_on_cls or based_on_cls's parents -> Can use with based_on_cls's instance

        :param func:
        :param based_on_cls:
        """
        if isinstance(func, str):
            func = getattr(based_on_cls, func, None)
            if not func:
                raise ValidatorMissing(based_on_cls, func)
        else:
            print(f"Validator __init__. func: {func}", getattr(based_on_cls, func.__name__, None))
            cls_func = getattr(based_on_cls, func.__name__, None)
            if cls_func:
                if cls_func is not func:
                    based_on_cls = EmptyValue.FIELD
            else:
                based_on_cls = EmptyValue.FIELD
        self.func = func
        self.based_on_cls = based_on_cls

    @staticmethod
    def get_hash(cls, func):
        return hash((cls, func))

    def __hash__(self):
        return self.get_hash(self.based_on_cls, self.func)

    def __repr__(self):
        return f"Validator(cls={self.based_on_cls}, func={self.func})"

    def is_bound_method(self):
        return is_field_exist(self.based_on_cls)

    def __call__(self, *args, **kwargs):
        print(f"self.func: {self.func}, based_on_cls: {self.based_on_cls}, args: {args}. kwargs: {kwargs}")
        return self.func(*args, **kwargs)
