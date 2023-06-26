from abc import ABC, abstractmethod
from typing import Any

from pyanhmi import AttributeManager
from pyanhmi.Config import Config, Mode


def register_attribute(cls):
    AttributeManager.CACHED_ATTRIBUTES.update({cls_type: cls for cls_type in cls.TYPES})
    # print(f"cls: {cls}, cls.SUPPORT_TYPES {AttributeManager.CACHED_ATTRIBUTES}")
    return cls


class Attribute(ABC):
    def __init__(self, field_type):
        self.field_type = field_type

    def __lt__(self, other):
        return self.get_att_priority() < other.get_att_priority()

    def __repr__(self):
        # print(f"ObjectAttribute: __repr__ ",  f"{self.__class__.__name__}({self.field_type})")
        return f"{self.__class__.__name__}({self.field_type})"

    def get_TypeManager(self, value_type):
        return AttributeManager.get_cached_attribute(value_type)

    def create(self, data: Any, mode: Mode):
        if mode is Mode.CASTING:
            return self.casting_create(data)
        if mode is Mode.STRICT:
            return self.strict_create(data)
        if mode is Mode.DUCK:
            return data

    @abstractmethod
    def strict_create(self, data):
        pass

    @abstractmethod
    def casting_create(self, data):
        pass
