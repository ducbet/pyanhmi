import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute
from pyanhmi.Attributes.PrimitiveAttribute import PrimitiveAttribute


@register_attribute
@dataclass
class StrAttribute(PrimitiveAttribute):
    TYPES: typing.ClassVar[list] = [str]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return super().__repr__()

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        # print(f"StrAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def duck_create(self, data):
        return data

    def strict_create(self, data):
        if not isinstance(data, str):
            raise TypeError(f"data is not str: data: {data}")
        return str(data)

    def casting_create(self, data):
        return str(data)
