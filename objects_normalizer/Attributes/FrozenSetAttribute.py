import typing
from collections.abc import Iterable
from dataclasses import dataclass

from objects_normalizer.Attributes.Attribute import register_attribute
from objects_normalizer.Attributes.SetAttribute import SetTypeAttribute


@register_attribute
@dataclass
class FrozenSetTypeAttribute(SetTypeAttribute):
    TYPES: typing.ClassVar[list] = [typing.FrozenSet, frozenset]

    def __init__(self, field_type):
        super().__init__(field_type)

    def get_att_priority(self):
        return super().get_att_priority()

    def get_hash_content(self):
        return super().get_hash_content()

    def __hash__(self):
        return super().__hash__()

    def create(self, data: dict):
        if not isinstance(data, Iterable):
            raise TypeError(f"data is not Iterable: data: {data}")
        return frozenset([self.value_att.create(v) for v in data])

    def __repr__(self):
        return super().__repr__()
