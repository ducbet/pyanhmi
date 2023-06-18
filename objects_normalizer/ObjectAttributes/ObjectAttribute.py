from objects_normalizer import TypeCheckManager
from objects_normalizer.Config import Config
from objects_normalizer.ObjectCreator import ObjectCreator


def register_att(cls):
    if not Config.DISCRIMINATE_PRIMITIVE_TYPES and getattr(cls, "IS_PRIMITIVE_TYPE", False):
        return cls

    TypeCheckManager.SUPPORT_TYPES.update({cls_type: cls for cls_type in cls.TYPES})
    print(f"cls: {cls}, cls.SUPPORT_TYPES {TypeCheckManager.SUPPORT_TYPES}")
    return cls


class ObjectAttribute:
    def __init__(self, field_type):
        self.field_type = field_type

    def __lt__(self, other):
        return self.get_att_priority() < other.get_att_priority()

    def get_TypeManager(self, value_type):
        print()
        print(f"TypeCheckManager.SUPPORT_TYPES: {TypeCheckManager.SUPPORT_TYPES}")
        print(f"value_type: {value_type}, TypeCheckManager.get_TypeManager(value_type): {TypeCheckManager.get_TypeManager(value_type)}")
        return TypeCheckManager.get_TypeManager(value_type)