import copy
import typing
from collections import OrderedDict
from typing import Any

from common.Config import Config, Mode, EmptyValue, is_field_exist
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype
from actions.Action import Action


class Field:
    def __init__(self, name: str = EmptyValue.FIELD,
                 attribute_type: Any = EmptyValue.FIELD,
                 is_class_var: bool = False,
                 alias: str = None,
                 is_ignored: bool = False,
                 getter_func: str = None,
                 mode: Mode = EmptyValue.FIELD,
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
        self.mode = mode if is_field_exist(mode) else Config.MODE
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
        if self._getter_func:
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

    # def create_actions(self, action_funcs: typing.List[typing.Union[str, typing.Callable]]) -> typing.Dict[int, Action]:
    #     actions = {}
    #     for action_func in action_funcs:
    #         action = Action(action_func, self.based_on_cls, self.name)
    #         actions[action.__hash__] = action
    #     return actions

    def get_attribute(self):
        return CookbookAttributes.get(self.attribute_type)

    def create(self, data, mode: Mode = EmptyValue.FIELD):
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
               f"getter_func_name: {self.getter_func})"

    @staticmethod
    def copy(cls, other: "Field"):
        params = copy.deepcopy(other.__dict__)
        return cls(**params)

    @staticmethod
    def updated(cls, field_1: "Field", field_2: "Field"):
        # if not isinstance(other, Field):
        #     raise InvalidDatatype(expects=Field, data=other)
        new_field = Field.copy(cls, field_1)

        new_field.name = field_2.name if Field.is_a_value(field_2.name) else new_field.name
        new_field.alias = field_2.alias if field_2.alias else new_field.alias
        new_field.getter_func = field_2.getter_func if field_2.getter_func else new_field.getter_func
        new_field.is_ignored = field_2.is_ignored if field_2.is_ignored else new_field.is_ignored
        new_field.attribute_type = field_2.attribute_type if Field.is_a_value(field_2.attribute_type) else new_field.attribute_type
        new_field.is_final = field_2.is_final if Field.is_a_value(field_2.is_final) else new_field.is_final
        new_field.is_class_var = field_2.is_class_var if Field.is_a_value(field_2.is_class_var) else new_field.is_class_var
        new_field.mode = field_2.mode  # todo check is it ok? check config mode???
        new_field.default = field_2.default if Field.is_a_value(field_2.default) else new_field.default

        new_field.pre_action_funcs.extend(field_2.pre_action_funcs)
        new_field.post_action_funcs.extend(field_2.pre_action_funcs)
        return new_field

    @staticmethod
    def is_final_type(value_type):
        origin_type = typing.get_origin(value_type)
        if origin_type == typing.Final:
            return True
        return False

    @staticmethod
    def is_a_value(val):
        # print(f"is_a_value val: {val}, EmptyValue.FIELD: {EmptyValue.FIELD}")
        return is_field_exist(val)
