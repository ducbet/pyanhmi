import typing
from collections import OrderedDict
from dataclasses import dataclass

from pyanhmi.Config import Config
from pyanhmi.Attributes.DictAttribute import DictAttribute
from pyanhmi.Attributes.Attribute import register_attribute
from pyanhmi.Error import InvalidDatatype


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

    def duck_create(self, data: typing.Any):
        try:
            if isinstance(data, dict):
                # the order of provided data is lost if data is dict
                return OrderedDict({self.key_att.duck_create(k): self.value_att.duck_create(v) for k, v in data.items()})
            if isinstance(data, list):
                # accept list of key-value. E.g: OrderedDict([('b',2), ('a', 1)])
                # the order of provided data is retained if data is list of tuple
                return OrderedDict([(self.key_att.duck_create(k_v[0]), self.value_att.duck_create(k_v[1])) for k_v in data])
        except:
            return data

    def strict_create(self, data):
        if isinstance(data, dict):
            # the order of provided data is lost if data is dict
            return OrderedDict({self.key_att.strict_create(k): self.value_att.strict_create(v) for k, v in data.items()})
        if isinstance(data, list):
            # accept list of key-value. E.g: OrderedDict([('b',2), ('a', 1)])
            # the order of provided data is retained if data is list of tuple
            return OrderedDict([(self.key_att.strict_create(k_v[0]), self.value_att.strict_create(k_v[1])) for k_v in data])
        raise InvalidDatatype(expects=[dict, f"list of key-value {tuple}"], data=data)

    def casting_create(self, data):
        if isinstance(data, dict):
            # the order of provided data is lost if data is dict
            return OrderedDict({self.key_att.casting_create(k): self.value_att.casting_create(v) for k, v in data.items()})
        if isinstance(data, list):
            # accept list of key-value. E.g: OrderedDict([('b',2), ('a', 1)])
            # the order of provided data is retained if data is list of tuple
            return OrderedDict([(self.key_att.casting_create(k_v[0]), self.value_att.casting_create(k_v[1])) for k_v in data])
        raise InvalidDatatype(expects=[dict, f"list of key-value {tuple}"], data=data)
