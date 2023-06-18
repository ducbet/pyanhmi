import typing
from dataclasses import dataclass

from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.ObjectAttribute import ObjectAttribute, register_att


@register_att
@dataclass
class AnyTypeAttribute(ObjectAttribute):
    TYPES = [typing.Any]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return f"AnyAtt()"

    def get_att_priority(self):
        return Config.AnyAtt_priority

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        return hash(self.get_hash_content())

    @staticmethod
    def create(data: dict):
        return data
