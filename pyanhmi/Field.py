import typing
from typing import Any

from common.Config import Config, Mode
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype


class Field:
    def __init__(self, name: str = None,
                 attribute_type: Any = None,
                 is_class_var: bool = False,
                 alias: str = None,
                 is_ignored: bool = False,
                 getter_func: str = None,
                 mode: Mode = None,
                 default: Any = None):
        self.name = name
        self.alias = alias
        self.getter_func = getter_func
        self.is_ignored = is_ignored
        self.attribute_type = attribute_type
        self.is_final = self.is_final_type(attribute_type)
        self.is_class_var = is_class_var
        self.mode = mode
        self.default = default

    @property
    def alias(self) -> str:
        if not self._alias:
            return self.name
        return self._alias

    @alias.setter
    def alias(self, alias):
        self._alias = alias

    @property
    def getter_func(self) -> str:
        if not self._getter_func:
            return self.name
        return self._getter_func

    @getter_func.setter
    def getter_func(self, func_name):
        self._getter_func = func_name

    @property
    def attribute_type(self) -> str:
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        self._attribute_type = attribute_type
        self._auto_init = self.get_attribute()

    def get_attribute(self):
        return CookbookAttributes.get(self.attribute_type)

    def decide_mode(self, mode: Mode) -> Mode:
        if mode:
            return mode
        if self.mode:
            return self.mode
        return Config.MODE

    def create(self, data, mode: Mode = None):
        return self._auto_init.create(data, self.decide_mode(mode))

    def __eq__(self, other: "Field"):
        return self.alias == other.alias and self.getter_func == other.getter_func

    def __repr__(self):
        return f"Field(" \
               f"name: {self.name}, " \
               f"alias: {self.alias}, " \
               f"attribute_type: {self.attribute_type}, " \
               f"default: {self.default}, " \
               f"is_class_var: {self.is_class_var}, " \
               f"auto_init: {self._auto_init}, " \
               f"mode: {self.mode}, " \
               f"getter_func_name: {self.getter_func})"

    def update(self, other: "Field"):
        if not isinstance(other, Field):
            raise InvalidDatatype(expects=Field, data=other)

        self.name = other.name if other.name else self.name
        self.alias = other.alias if other.alias else self.alias
        self.getter_func = other.getter_func if other.getter_func else self.getter_func
        self.is_ignored = other.is_ignored if other.is_ignored else self.is_ignored
        self.attribute_type = other.attribute_type if other.attribute_type else self.attribute_type
        self.is_final = other.is_final if other.is_final else self.is_final
        self.is_class_var = other.is_class_var if other.is_class_var else self.is_class_var
        self.mode = other.mode if other.mode else self.mode

    @staticmethod
    def is_final_type(value_type):
        origin_type = typing.get_origin(value_type)
        if origin_type == typing.Final:
            return True
        return False
