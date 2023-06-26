import typing
from collections import OrderedDict
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute
from pyanhmi.Attributes.DictAttribute import DictAttribute
from pyanhmi.Config import Config


@register_attribute
@dataclass
class OrderedDictAttribute(DictAttribute):
    TYPES: typing.ClassVar[list] = [typing.OrderedDict, OrderedDict]

    def __init__(self, field_type):
        super().__init__(field_type)

    @property
    def value_constructor(self):
        origin_type = typing.get_origin(self.value_type)
        # print(f"value_constructor: {self.value_type}, origin_type: {origin_type}")
        return origin_type if origin_type else self.value_type

    def get_att_priority(self):
        return max(Config.OrderedDict_priority, self.key_att.get_att_priority(), self.value_att.get_att_priority())

    def get_hash_content(self):
        return super().get_hash_content()

    def __hash__(self):
        return super().__hash__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key_att}, {self.value_att})"

    def strict_create(self, data):
        return OrderedDict(super().strict_create(data))

    def casting_create(self, data):
        return OrderedDict(super().casting_create(data))
