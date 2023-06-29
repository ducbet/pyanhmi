import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import Attribute
from common.Config import Config
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes


@CookbookAttributes.add
@dataclass
class AnyAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [typing.Any]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        # print(f"AnyTypeAttribute __repr__ ", f"{self.__class__.__name__}({self.field_type})")
        return f"{self.__class__.__name__}({self.field_type})"

    def get_att_priority(self):
        return Config.AnyAtt_priority

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        return hash(self.get_hash_content())

    def strict_create(self, data):
        return data

    def casting_create(self, data):
        return data

