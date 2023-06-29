import typing
from dataclasses import dataclass

from pyanhmi.Attributes.PrimitiveAttribute import PrimitiveAttribute
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype


@CookbookAttributes.add
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

    def strict_create(self, data: int):
        if not isinstance(data, int):
            raise InvalidDatatype(expects=int, data=data)
        return data

    def casting_create(self, data):
        try:
            return int(data)
        except (ValueError, TypeError):
            # ValueError: int("asd")
            # TypeError: int(None)
            raise InvalidDatatype(expects=int, data=data)
