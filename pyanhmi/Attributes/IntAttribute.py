import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute
from pyanhmi.Attributes.PrimitiveAttribute import PrimitiveAttribute
from pyanhmi.Config import Mode
from pyanhmi.Error import InvalidDatatype


@register_attribute
@dataclass
class IntAttribute(PrimitiveAttribute):
    TYPES: typing.ClassVar[list] = [int]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return super().__repr__()

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        # print(f"IntAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def duck_create(self, data: typing.Any):
        return data

    def strict_create(self, data: int):
        if not isinstance(data, int):
            raise InvalidDatatype(expects=int, data=data)
        return int(data)

    def casting_create(self, data):
        return int(data)
