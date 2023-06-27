import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute
from pyanhmi.Attributes.PrimitiveAttribute import PrimitiveAttribute
from pyanhmi.Config import Mode
from pyanhmi.Error import InvalidDatatype


@register_attribute
@dataclass
class FloatAttribute(PrimitiveAttribute):
    TYPES: typing.ClassVar[list] = [float]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return super().__repr__()

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        return hash(self.get_hash_content())

    def strict_create(self, data: float):
        if not isinstance(data, float):
            raise InvalidDatatype(expects=float, data=data)
        return data

    def casting_create(self, data):
        try:
            return float(data)
        except (ValueError, TypeError):
            raise InvalidDatatype(expects=float, data=data)
