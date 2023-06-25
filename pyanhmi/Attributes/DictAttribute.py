import inspect
import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute, Attribute
from pyanhmi.Config import Config


@register_attribute
@dataclass
class DictAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [dict]

    def __init__(self, field_type):
        super().__init__(field_type)
        args_type = typing.get_args(field_type)
        if not args_type:
            self.key_att = self.get_TypeManager(None)(None)
            self.value_att = self.get_TypeManager(None)(None)
            return
        self.key_type = args_type[0]
        self.key_att = self.get_TypeManager(self.key_type)(self.key_type)
        self.value_type = args_type[1]
        self.value_att = self.get_TypeManager(self.value_type)(self.value_type)

    def get_att_priority(self):
        return max(Config.DictAtt_priority, self.key_att.get_att_priority(), self.value_att.get_att_priority())

    def get_hash_content(self):
        return self.__class__, self.key_att.get_hash_content(), self.value_att.get_hash_content()

    def __hash__(self):
        # print(f"DictAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key_att}, {self.value_att})"

    def duck_create(self, data):
        try:
            return {self.key_att.duck_create(k): self.value_att.duck_create(v) for k, v in data.items()}
        except:
            return data

    def strict_create(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError(f"data is not dict: data: {data}")
        return {self.key_att.strict_create(k): self.value_att.strict_create(v) for k, v in data.items()}

    def casting_create(self, data):
        return {self.key_att.casting_create(k): self.value_att.casting_create(v) for k, v in data.items()}
