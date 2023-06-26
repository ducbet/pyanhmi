import typing
from collections.abc import Iterable
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute
from pyanhmi.Attributes.SetAttribute import SetAttribute
from pyanhmi.Error import InvalidDatatype


@register_attribute
@dataclass
class FrozenSetAttribute(SetAttribute):
    TYPES: typing.ClassVar[list] = [typing.FrozenSet, frozenset]

    def __init__(self, field_type):
        super().__init__(field_type)

    def get_att_priority(self):
        return super().get_att_priority()

    def get_hash_content(self):
        return super().get_hash_content()

    def __hash__(self):
        return super().__hash__()

    def __repr__(self):
        return super().__repr__()

    def strict_create(self, data):
        if not isinstance(data, Iterable):
            raise InvalidDatatype(expects=Iterable, data=data)
        return frozenset([self.value_att.strict_create(v) for v in data])

    def casting_create(self, data):
        return frozenset([self.value_att.casting_create(v) for v in data])

