import typing
from dataclasses import dataclass

from pyanhmi.Attributes.PrimitiveAttribute import PrimitiveAttribute
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype


@CookbookAttributes.add
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

    def strict_create(self, data):
        if not isinstance(data, str):
            raise InvalidDatatype(expects=str, data=data)
        return data

    def casting_create(self, data):
        try:
            return str(data)
        except Exception:
            raise InvalidDatatype(expects=str, data=data)
    def duck_test_create(self, data):
        return data