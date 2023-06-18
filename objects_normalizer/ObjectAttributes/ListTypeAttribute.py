import typing
from dataclasses import dataclass

from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.ObjectAttribute import register_att, ObjectAttribute


@register_att
@dataclass
class ListTypeAttribute(ObjectAttribute):
    TYPES = [list]

    def __init__(self, field_type):
        super().__init__(field_type)
        args_type = typing.get_args(field_type)
        self.value_att = self.get_TypeManager(args_type[0])(args_type[0])

    def get_att_priority(self):
        return max(Config.ListAtt_priority, self.value_att.get_att_priority())

    def __repr__(self):
        return f"ListAtt({self.value_att})"

    def get_hash_content(self):
        return self.__class__, self.value_att.get_hash_content()

    def __hash__(self):
        print(f"ListAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def create(self, data):
        if not isinstance(data, list):
            raise TypeError(f"data is not list: data: {data}")
        return [self.value_att.create(v) for v in data]
