import typing
from dataclasses import dataclass

from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.ObjectAttribute import register_attribute, ObjectAttribute


@register_attribute
@dataclass
class TupleTypeAttribute(ObjectAttribute):
    TYPES: typing.ClassVar[list] = [tuple]
    priority = Config.TupleAtt_priority

    def __init__(self, field_type):
        super().__init__(field_type)
        self.value_atts = []
        for arg_type in typing.get_args(field_type):
            self.value_atts.append(self.get_TypeManager(arg_type)(arg_type))

    def get_att_priority(self):
        if not self.value_atts:
            return Config.TupleAtt_priority
        return max(Config.TupleAtt_priority, *[field.get_att_priority() for field in self.value_atts])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value_atts})"

    def get_hash_content(self):
        hash_content = [self.__class__]
        for field in self.value_atts:
            hash_content.append(field.get_hash_content())
        return tuple(hash_content)

    def __hash__(self):
        # print(f"TupleAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def create(self, data: tuple):
        if not self.value_atts:
            return data
        return tuple(self.value_atts[i].create(val) for i, val in enumerate(data))
