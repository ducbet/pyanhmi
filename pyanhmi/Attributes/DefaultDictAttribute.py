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

    @property
    def value_constructor(self):
        origin_type = typing.get_origin(self.value_type)
        # print(f"value_constructor: {self.value_type}, origin_type: {origin_type}")
        return origin_type if origin_type else self.value_type

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
            data = {self.key_att.duck_create(k): self.value_att.duck_create(v) for k, v in data.items()}
            return defaultdict(self.value_constructor, data)
        except:
            return data

    def strict_create(self, data: defaultdict):
        if not isinstance(data, defaultdict):
            raise TypeError(f"data is not defaultdict: data: {data}")
        dict_data = {self.key_att.strict_create(k): self.value_att.strict_create(v) for k, v in data.items()}
        return defaultdict(self.value_constructor, dict_data)

    def casting_create(self, data):
        data = {self.key_att.casting_create(k): self.value_att.casting_create(v) for k, v in data.items()}
        return defaultdict(self.value_constructor, data)
