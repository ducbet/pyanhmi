import typing
from dataclasses import dataclass

from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.AnyTypeAttribute import AnyTypeAttribute
from objects_normalizer.ObjectAttributes.ObjectAttribute import ObjectAttribute, register_attribute


@register_attribute
@dataclass
class UnionTypeAttribute(ObjectAttribute):
    TYPES: typing.ClassVar[list] = [typing.Union]

    def __init__(self, field_type):
        super().__init__(field_type)
        self.value_atts = set()
        for arg in typing.get_args(field_type):
            self.value_atts.add(self.get_TypeManager(arg)(arg))
        if AnyTypeAttribute in self.value_atts:
            self.value_atts.remove(AnyTypeAttribute)
            self.value_atts = list(self.value_atts)
            self.value_atts.append(AnyTypeAttribute)
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

    def create(self, data: typing.Any):
        for t in self.value_atts:
            try:
                return t.create(data)
            except TypeError:
                pass
        return data
