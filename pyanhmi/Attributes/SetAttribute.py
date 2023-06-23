import typing
from dataclasses import dataclass

from pyanhmi.Config import Config
from pyanhmi.Attributes.Attribute import register_attribute, Attribute


@register_attribute
@dataclass
class SetTypeAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [set]

    def __init__(self, field_type):
        super().__init__(field_type)
        args_type = typing.get_args(field_type)
        if not args_type:
            self.value_att = self.get_TypeManager(None)
            return
        self.value_att = self.get_TypeManager(args_type[0])(args_type[0])

    def get_att_priority(self):
        return max(Config.SetAtt_priority, self.value_att.get_att_priority())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value_att})"

    def get_hash_content(self):
        return self.__class__, self.value_att.get_hash_content()

    def __hash__(self):
        return hash(self.get_hash_content())

    def create(self, data):
        if not isinstance(data, set):
            raise TypeError(f"data is not set: data: {data}")
        # print(f"{self.__class__} self.value_att: {self.value_att}, data: {data}")
        return set(self.value_att.create(v) for v in data)
