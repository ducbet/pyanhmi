import typing
from typing import Any

from common.Config import Config, Mode, EmptyValue
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype


class Field:
    def __init__(self, name: str = EmptyValue.FIELD,
                 attribute_type: Any = EmptyValue.FIELD,
                 is_class_var: bool = EmptyValue.FIELD,
                 alias: str = EmptyValue.FIELD,
                 is_ignored: bool = EmptyValue.FIELD,
                 getter_func: str = EmptyValue.FIELD,
                 mode: Mode = EmptyValue.FIELD,
                 default: Any = EmptyValue.FIELD):
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
        # print()
        # print(f"property._alias: {self._alias}, {Field.is_a_value(self._alias)}")
        if not Field.is_a_value(self._alias):
            return self.name
        return self._alias

    @alias.setter
    def alias(self, alias):
        self._alias = alias
        # print(f"@alias.setter self._alias: {self._alias}")

    @property
    def getter_func(self) -> str:
        if not Field.is_a_value(self._getter_func):
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
        if Field.is_a_value(mode):
            return mode
        if Field.is_a_value(self.mode):
            return self.mode
        return Config.MODE

    def create(self, data, mode: Mode = EmptyValue.FIELD):
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
        self.name = other.name if Field.is_a_value(other.name) else self.name
        self.alias = other.alias if Field.is_a_value(other.alias) else self.alias
        self.getter_func = other.getter_func if Field.is_a_value(other.getter_func) else self.getter_func
        self.is_ignored = other.is_ignored if Field.is_a_value(other.is_ignored) else self.is_ignored
        self.attribute_type = other.attribute_type if Field.is_a_value(other.attribute_type) else self.attribute_type
        self.is_final = other.is_final if Field.is_a_value(other.is_final) else self.is_final
        self.is_class_var = other.is_class_var if Field.is_a_value(other.is_class_var) else self.is_class_var
        self.mode = other.mode if Field.is_a_value(other.mode) else self.mode
        self.default = other.default if Field.is_a_value(other.default) else self.default

    @staticmethod
    def is_final_type(value_type):
        origin_type = typing.get_origin(value_type)
        if origin_type == typing.Final:
            return True
        return False

    @staticmethod
    def is_a_value(val):
        # print(f"is_a_value val: {val}, EmptyValue.FIELD: {EmptyValue.FIELD}")
        return val is not EmptyValue.FIELD
