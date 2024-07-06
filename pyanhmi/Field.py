import copy
import typing
from typing import Any

from common.Config import Config, CastingMode, EmptyValue, is_field_exist
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes


class Field:
    def __init__(self, name: str = None,
                 attribute_type: Any = EmptyValue.FIELD,
                 is_class_var: bool = False,
                 alias: str = None,
                 is_ignored: bool = False,
                 getter_func: str = None,
                 mode: CastingMode = None,
                 default: Any = EmptyValue.FIELD,
                 pre_actions: typing.List = None,
                 post_actions: typing.List = None,
                 based_on_cls: type[Any] = None
                 ):
        self.name = name
        self.alias = alias
        self.getter_func = getter_func
        self.is_ignored = is_ignored
        self.attribute_type = attribute_type
        self.is_final = self.is_final_type(attribute_type)
        self.is_class_var = is_class_var
        self.mode = mode if mode else Config.MODE
        self.default = default
        self.based_on_cls = based_on_cls  # can be None when defined by user
        self.pre_action_funcs: list = pre_actions if pre_actions else []
        self.pre_actions = []
        self.post_action_funcs: list = post_actions if post_actions else []
        self.post_actions = []

    @property
    def alias(self) -> str:
        if not self._alias:
            return self.name
        return self._alias

    @alias.setter
    def alias(self, alias: str) -> None:
        self._alias = alias

    @property
    def getter_func(self) -> str:
        # print()
        # print(f"self._getter_func: {self._getter_func}")
        # print(f"self.name: {self.name}")
        if not self._getter_func:
            # print(f"self.name: {self.name}")
            return self.name
        return self._getter_func

    @getter_func.setter
    def getter_func(self, func_name) -> None:
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

    def create(self, data, mode: CastingMode = EmptyValue.FIELD):
        return self._auto_init.create(data, mode if mode else self.mode)

    def __eq__(self, other: "Field"):
        # todo check again???
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
               f"getter_func: {self.getter_func})"

    @staticmethod
    def copy(cls, other: "Field"):
        # params = {k: v for k, v in copy.deepcopy(other.__dict__).items() if not k.startswith("_")}
        # print(params)
        # return cls(**params)
        return copy.deepcopy(other)

    @staticmethod
    def updated(cls, field_1: "Field", field_2: "Field"):
        # if not isinstance(other, Field):
        #     raise InvalidDatatype(expects=Field, data=other)
        new_field = Field.copy(cls, field_1)

        new_field.name = field_2.name if field_2.name else new_field.name
        new_field.alias = field_2.alias if field_2.alias else new_field.alias
        new_field.getter_func = field_2.getter_func if field_2.getter_func else new_field.getter_func
        new_field.is_ignored = field_2.is_ignored if field_2.is_ignored else new_field.is_ignored
        new_field.attribute_type = field_2.attribute_type if Field.is_a_value(field_2.attribute_type) else new_field.attribute_type
        new_field.is_final = field_2.is_final if field_2.is_final else new_field.is_final
        new_field.is_class_var = field_2.is_class_var if field_2.is_class_var else new_field.is_class_var
        # print(f"field_1.mode: {field_1.mode}")
        # print(f"field_2.mode: {field_2.mode}")
        new_field.mode = field_2.mode  # todo check is it ok? check config mode???
        new_field.default = field_2.default if Field.is_a_value(field_2.default) else new_field.default

        new_field.pre_action_funcs.extend(field_2.pre_action_funcs)
        new_field.post_action_funcs.extend(field_2.post_action_funcs)
        return new_field

    @staticmethod
    def is_final_type(value_type) -> bool:
        origin_type = typing.get_origin(value_type)
        if origin_type == typing.Final:
            return True
        return False

    @staticmethod
    def is_a_value(val):
        # print(f"is_a_value val: {val}, EmptyValue.FIELD: {EmptyValue.FIELD}")
        return is_field_exist(val)
