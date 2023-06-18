from dataclasses import dataclass

from objects_normalizer.ObjectAttributes.ObjectAttribute import register_att
from objects_normalizer.ObjectAttributes.PrimitiveTypeAttribute import PrimitiveTypeAttribute


@register_att
@dataclass
class IntTypeAttribute(PrimitiveTypeAttribute):
    TYPES = [int]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return f"IntAtt()"

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        print(f"IntAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def create(self, data: int):
        if not isinstance(data, int):
            raise TypeError(f"data is not int: data: {data}")
        return data
