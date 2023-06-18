from dataclasses import dataclass

from objects_normalizer.ObjectAttributes.ObjectAttribute import register_att
from objects_normalizer.ObjectAttributes.PrimitiveTypeAttribute import PrimitiveTypeAttribute


@register_att
@dataclass
class StrTypeAttribute(PrimitiveTypeAttribute):
    TYPES = [str]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return f"StrAtt()"

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        print(f"StrAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def create(self, data: str):
        if not isinstance(data, str):
            raise TypeError(f"data is not str: data: {data}")
        return data
