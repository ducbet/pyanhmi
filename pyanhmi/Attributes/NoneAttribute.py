import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import Attribute
from common.Config import Config
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype


@CookbookAttributes.add
@dataclass
class NoneAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [None]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.field_type})"

    def get_att_priority(self):
        return Config.NoneAtt_priority

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        return hash(self.get_hash_content())

    def strict_create(self, data):
        if data is not None:
            raise InvalidDatatype(expects=None, data=data)
        return data

    def casting_create(self, data):
        return None

