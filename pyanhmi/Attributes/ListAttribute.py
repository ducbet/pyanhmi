import typing
from dataclasses import dataclass

from pyanhmi.Config import Config
from pyanhmi.Attributes.Attribute import register_attribute, Attribute
from pyanhmi.Error import InvalidDatatype


@register_attribute
@dataclass
class ListAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [list]

    def __init__(self, field_type):
        super().__init__(field_type)
        args_type = typing.get_args(field_type)
        if not args_type:
            self.value_att = self.get_TypeManager(None)(None)
            return
        self.value_att = self.get_TypeManager(args_type[0])(args_type[0])

    def get_att_priority(self):
        return max(Config.ListAtt_priority, self.value_att.get_att_priority())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value_att})"

    def get_hash_content(self):
        return self.__class__, self.value_att.get_hash_content()

    def __hash__(self):
        # print(f"ListAtt: self.field_type: {self.field_type}, {hash(self.get_hash_content())}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def duck_create(self, data):
        try:
            return list(self.value_att.duck_create(v) for v in data)
        except:
            return data

    def strict_create(self, data: list):
        if not isinstance(data, list):
            raise InvalidDatatype(expects=list, data=data)
        # print(f"{self.__class__} self.value_att: {self.value_att}, data: {data}")
        return list(self.value_att.strict_create(v) for v in data)

    def casting_create(self, data):
        return list(self.value_att.casting_create(v) for v in data)
