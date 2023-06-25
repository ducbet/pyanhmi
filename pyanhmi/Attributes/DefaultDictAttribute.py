import typing
from collections import defaultdict
from dataclasses import dataclass

from pyanhmi.Attributes.DictAttribute import DictAttribute
from pyanhmi.Attributes.Attribute import register_attribute


@register_attribute
@dataclass
class DefaultDictAttribute(DictAttribute):
    TYPES: typing.ClassVar[list] = [typing.DefaultDict, defaultdict]

    def __init__(self, field_type):
        super().__init__(field_type)

    def get_default_factory(self, value_type):
        origin_type = typing.get_origin(value_type)
        default_factory = origin_type if origin_type else value_type
        if origin_type is defaultdict:
            nested_value_type = typing.get_args(value_type)[1]
            nested_value_constructor = self.get_default_factory(nested_value_type)
            default_factory = defaultdict(nested_value_constructor)
            return lambda: default_factory
        return default_factory

    def get_att_priority(self):
        return super().get_att_priority()

    def get_hash_content(self):
        return super().get_hash_content()

    def __hash__(self):
        return super().__hash__()

    def __repr__(self):
        return super().__repr__()

    def duck_create(self, data: typing.Any):
        try:
            return defaultdict(self.get_default_factory(self.value_type), super().duck_create(data))
        except:
            return data

    def strict_create(self, data: defaultdict):
        return defaultdict(self.get_default_factory(self.value_type), super().strict_create(data))

    def casting_create(self, data):
        return defaultdict(self.get_default_factory(self.value_type), super().casting_create(data))
