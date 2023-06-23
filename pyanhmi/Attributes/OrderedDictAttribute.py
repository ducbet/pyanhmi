import typing
from collections import OrderedDict
from dataclasses import dataclass

from pyanhmi.Config import Config
from pyanhmi.Attributes.DictAttribute import DictTypeAttribute
from pyanhmi.Attributes.Attribute import register_attribute


@register_attribute
@dataclass
class OrderedDictTypeAttribute(DictTypeAttribute):
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

    def create(self, data: dict):
        if isinstance(data, dict):
            # the order of provided data is lost if data is dict
            return OrderedDict({self.key_att.create(k): self.value_att.create(v) for k, v in data.items()})
        if isinstance(data, list):
            # accept list of key-value. E.g: OrderedDict([('b',2), ('a', 1)])
            # the order of provided data is retained if data is list of tuple
            return OrderedDict([(self.key_att.create(k_v[0]), self.value_att.create(k_v[1])) for k_v in data])
        raise TypeError(f"data is not dict or list of key-value tuple: data: {data}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key_att}, {self.value_att})"
