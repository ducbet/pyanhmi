from abc import ABC
from dataclasses import dataclass
from typing import ClassVar

from common.Config import Config
from pyanhmi.Attributes.Attribute import Attribute


@dataclass
class PrimitiveAttribute(Attribute, ABC):
    IS_PRIMITIVE_TYPE: ClassVar[bool] = True

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return super().__repr__()

    def get_att_priority(self):
        return Config.PRIMITIVE_TYPE_PRIORITY
