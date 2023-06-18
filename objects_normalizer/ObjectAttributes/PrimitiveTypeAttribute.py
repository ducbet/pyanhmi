from dataclasses import dataclass
from typing import ClassVar

from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.ObjectAttribute import ObjectAttribute


@dataclass
class PrimitiveTypeAttribute(ObjectAttribute):
    IS_PRIMITIVE_TYPE: ClassVar[bool] = True

    def __init__(self, field_type):
        super().__init__(field_type)

    def get_att_priority(self):
        return Config.PRIMITIVE_TYPE_PRIORITY
