from typing import Any

from pyanhmi.AttributeManager import AttributeManager


class Field:
    def __init__(self, name: str = None,
                 attribute_type: Any = None,
                 is_class_var: bool = None,
                 alias: str = None,
                 getter_func: str = None):
        self.name = name
        self.alias = alias
        self.getter_func = getter_func
        self.is_ignored = False
        self.attribute_type = attribute_type
        self.is_final = AttributeManager.is_final_type(attribute_type)
        self.is_class_var = is_class_var
        self.auto_init = self.get_attribute()

    def create(self, data):
        return self.auto_init.create(data)

    def get_attribute(self):
        return AttributeManager.get_cached_attribute(self.attribute_type)(self.attribute_type)

    @property
    def alias(self) -> str:
        if not self._normalized_field_name:
            return self.name
        return self._normalized_field_name

    @alias.setter
    def alias(self, normalized_field_name):
        self._normalized_field_name = normalized_field_name

    @property
    def getter_func(self) -> str:
        # print(f"@property getter_func_name, self._getter_func_name: {self._getter_func_name}")
        if not self._getter_func:
            # print(f"@property if not self._getter_func_name")
            return self.name
        return self._getter_func

    @getter_func.setter
    def getter_func(self, func_name):
        self._getter_func = func_name

    def __eq__(self, other: "Field"):
        return (self.alias == other.alias and self.getter_func == other.getter_func)

    def __repr__(self):
        return f"NormalizeRule(" \
               f"localized_field_name: {self.name}, " \
               f"field_type: {self.attribute_type}, " \
               f"is_class_var: {self.is_class_var}, " \
               f"auto_init: {self.auto_init}, " \
               f"normalized_field_name: {self.alias}, " \
               f"getter_func_name: {self.getter_func})"
