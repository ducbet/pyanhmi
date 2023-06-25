import typing
from dataclasses import dataclass
from enum import Enum

from pyanhmi.Config import Config, Mode
from pyanhmi.Attributes.AnyAttribute import AnyAttribute
from pyanhmi.Attributes.Attribute import Attribute, register_attribute


@register_attribute
@dataclass
class UnionAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [typing.Union]

    def __init__(self, field_type):
        super().__init__(field_type)
        self.value_atts = set()
        for arg in typing.get_args(field_type):
            self.value_atts.add(self.get_TypeManager(arg)(arg))
        if AnyAttribute in self.value_atts:
            self.value_atts.remove(AnyAttribute)
            self.value_atts = list(self.value_atts)
            self.value_atts.append(AnyAttribute)
        else:
            self.value_atts = list(self.value_atts)
        self.value_atts = sorted(self.value_atts, reverse=True)
        # print(f"UnionAtt: self.value_atts {self.value_atts}")

    def get_att_priority(self):
        if not self.value_atts:
            return Config.UnionAtt_priority
        return max(Config.UnionAtt_priority, *[field.get_att_priority() for field in self.value_atts])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value_atts})"

    def get_hash_content(self):
        hash_content = [self.__class__]
        for field in self.value_atts:
            hash_content.append(field.get_hash_content())
        return tuple(hash_content)

    def __hash__(self):
        # print(f"UnionAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def duck_create(self, data):
        try:
            for t in self.value_atts:
                try:
                    return t.duck_create(data)
                except TypeError:
                    pass
            return data
        except:
            return data

    def strict_create(self, data):
        for t in self.value_atts:
            try:
                return t.strict_create(data)
            except TypeError:
                pass
        return data

    def casting_create(self, data):
        for t in self.value_atts:
            try:
                return t.casting_create(data)
            except TypeError:
                pass
        return data
