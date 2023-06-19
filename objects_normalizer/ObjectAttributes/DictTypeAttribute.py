import typing
from collections import defaultdict, OrderedDict
from dataclasses import dataclass

from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.ObjectAttribute import register_attribute, ObjectAttribute


@register_attribute
@dataclass
class DictTypeAttribute(ObjectAttribute):
    TYPES: typing.ClassVar[list] = [dict]

    def __init__(self, field_type):
        super().__init__(field_type)
        args_type = typing.get_args(field_type)
        if not args_type:
            self.key_att = self.get_TypeManager(None)
            self.value_att = self.get_TypeManager(None)
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

    def create(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError(f"data is not dict: data: {data}")
        return {self.key_att.create(k): self.value_att.create(v) for k, v in data.items()}

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key_att}, {self.value_att})"
