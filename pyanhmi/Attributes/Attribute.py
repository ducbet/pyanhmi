from pyanhmi import AttributeManager
from pyanhmi.Config import Config


def register_attribute(cls):
    if not Config.DISCRIMINATE_PRIMITIVE_TYPES and getattr(cls, "IS_PRIMITIVE_TYPE", False):
        return cls

    AttributeManager.CACHED_ATTRIBUTES.update({cls_type: cls for cls_type in cls.TYPES})
    print(f"cls: {cls}, cls.SUPPORT_TYPES {AttributeManager.CACHED_ATTRIBUTES}")
    return cls


class Attribute:
    def __init__(self, field_type):
        self.field_type = field_type

    def __lt__(self, other):
        return self.get_att_priority() < other.get_att_priority()

    def __repr__(self):
        # print(f"ObjectAttribute: __repr__ ",  f"{self.__class__.__name__}({self.field_type})")
        return f"{self.__class__.__name__}({self.field_type})"

    def get_TypeManager(self, value_type):
        return AttributeManager.get_cached_attribute(value_type)