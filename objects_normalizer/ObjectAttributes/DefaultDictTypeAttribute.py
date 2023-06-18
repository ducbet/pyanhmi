import typing
from collections import defaultdict
from dataclasses import dataclass

from objects_normalizer.ObjectAttributes.DictTypeAttribute import DictTypeAttribute
from objects_normalizer.ObjectAttributes.ObjectAttribute import register_attribute


@register_attribute
@dataclass
class DefaultDictTypeAttribute(DictTypeAttribute):
    TYPES: typing.ClassVar[list] = [defaultdict]

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

    def create(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError(f"data is not dict: data: {data}")
        dict_data = {self.key_att.create(k): self.value_att.create(v) for k, v in data.items()}
        return defaultdict(self.value_constructor, dict_data)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key_att}, {self.value_att})"
