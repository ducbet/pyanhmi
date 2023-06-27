import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute
from pyanhmi.Attributes.PrimitiveAttribute import PrimitiveAttribute
from pyanhmi.Config import Mode
from pyanhmi.Error import InvalidDatatype


@register_attribute
@dataclass
class BoolAttribute(PrimitiveAttribute):
    TYPES: typing.ClassVar[list] = [bool]

    def __init__(self, field_type):
        super().__init__(field_type)

    def __repr__(self):
        return super().__repr__()

    def get_hash_content(self):
        return self.__class__

    def __hash__(self):
        return hash(self.get_hash_content())

    @staticmethod
    def cast_to_bool(data):
        """
        https://github.com/python/cpython/blob/v3.11.2/Lib/distutils/util.py#L308
        Convert a string representation of truth to True or False.
        True values are: 1, '1', 'y', 'yes', 't', 'true', 'on'
        False values are: 0, '0', 'n', 'no', 'f', 'false', 'off'
        Raises ValueError if 'val' is anything else.
        :return:
        """
        if isinstance(data, bool):
            return bool(data)
        try:
            data_str = str(data).lower()
            if data_str in ("1", "y", "yes", "t", "true", "on"):
                return True
            elif data_str in ("0", "n", "no", "f", "false", "off", "none"):
                return False
        except Exception:
            pass
        raise InvalidDatatype(expects=bool, data=data)

    def strict_create(self, data: bool):
        if not isinstance(data, bool):
            raise InvalidDatatype(expects=bool, data=data)
        return data

    def casting_create(self, data):
        return self.cast_to_bool(data)
