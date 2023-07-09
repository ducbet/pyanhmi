from dataclasses import dataclass

from common.Config import Config
from pyanhmi.Creator import create
from pyanhmi.Attributes.Attribute import Attribute


@dataclass
class CustomAttribute(Attribute):
    # this class is added to CookbookAttributes when creating AuthenticRecipe

    def __init__(self, field_type):
        super().__init__(field_type)

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

    def strict_create(self, data):
        return create(data, self.field_type)

    def casting_create(self, data):
        return create(data, self.field_type)

    def duck_test_create(self, data):
        return create(data, self.field_type)
