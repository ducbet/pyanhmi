from common.Config import EmptyValue, is_field_exist
from common.Error import ActionMissing


class Action:
    def __init__(self, func, based_on_cls, attr_name: str = None):
        """
        If func is string -> belongs to based_on_cls
        If func is function -> 2 possibilities
        1. If can not find func's name in cls -> unbounded function. getattr(based_on_cls, func.__name__, None) == None
        2. If can find func's name in cls -> Is method of based_on_cls or based_on_cls's parents -> Can use with based_on_cls's instance
        :param func:
        :param based_on_cls:
        """
        # print(f"func: {func}, based_on_cls: {based_on_cls}")
        if isinstance(func, str):
            func = getattr(based_on_cls, func, None)
            if not func:
                raise ActionMissing(based_on_cls, func)
        else:
            cls_func = getattr(based_on_cls, func.__name__, None)
            if cls_func:
                if cls_func is not func:
                    based_on_cls = EmptyValue.FIELD
            else:
                based_on_cls = EmptyValue.FIELD
        self.func = func
        self.based_on_cls = based_on_cls
        self.attr_name = attr_name  # only be used for unbounded actions

    @staticmethod
    def get_hash(cls, func):
        return hash((cls, func))

    def __hash__(self):
        return self.get_hash(self.based_on_cls, self.func)

    def __repr__(self):
        return f"{self.__class__.__name__}(cls={self.based_on_cls}, func={self.func})"

    # def is_bound_method(self):
    #     return is_field_exist(self.based_on_cls)

    def execute(self, obj):
        if not self.attr_name:
            return self.func(obj)
        # print()
        # print(f"self.attr_name: {self.attr_name}, self.func: {self.func}, based_on_cls: {self.based_on_cls}, obj: {obj}")
        value_before = getattr(obj, self.attr_name)
        value_after = self.func(obj, self.attr_name, value_before)
        setattr(obj, self.attr_name, value_after)
