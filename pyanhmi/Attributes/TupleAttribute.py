import typing
from dataclasses import dataclass

from pyanhmi.Config import Config
from pyanhmi.Attributes.Attribute import register_attribute, Attribute


@register_attribute
@dataclass
class TupleAttribute(Attribute):
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

    def duck_create(self, data):
        try:
            if not self.value_atts:
                return data
            return tuple(self.value_atts[i].duck_create(val) for i, val in enumerate(data))
        except:
            return data

    def strict_create(self, data):
        if not isinstance(data, tuple):
            raise TypeError(f"data is not tuple: data: {data}")
        if not self.value_atts:
            return data
        return tuple(self.value_atts[i].strict_create(val) for i, val in enumerate(data))

    def casting_create(self, data):
        if not self.value_atts:
            return data
        return tuple(self.value_atts[i].casting_create(val) for i, val in enumerate(data))
