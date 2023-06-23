import typing
from dataclasses import dataclass

from pyanhmi.Config import Config
from pyanhmi.Attributes.Attribute import Attribute, register_attribute
from pyanhmi.ObjectCreator import ObjectCreator


@register_attribute
@dataclass
class CustomTypeAttribute(Attribute):
    TYPES: typing.ClassVar[list] = ["CustomTypeAttribute"]  # special case

    def __init__(self, field_type):
        super().__init__(field_type)

    def create(self, data: dict):
        return ObjectCreator.create_obj(data, self.field_type)

    def get_att_priority(self):
        return Config.ObjAtt_priority

    def __repr__(self):
        return f"{self.__class__.__name__}({self.field_type})"

    def get_hash_content(self):
        # print(f"ObjAtt: get_hash_content: self.__class__ {self.__class__}, self.field_type: {self.field_type}")
        return self.__class__, self.field_type

    def __hash__(self):
        # print(f"ObjAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

