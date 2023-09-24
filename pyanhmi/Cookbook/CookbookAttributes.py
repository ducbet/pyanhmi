import functools
import os
import typing

from common.Config import Config
from pyanhmi.Attributes.Attribute import Attribute
from pyanhmi.Cookbook.Cookbook import Cookbook

T = typing.TypeVar("T")

class CookbookAttributes(Cookbook):
    ATTRIBUTES: typing.Dict[typing.Any, typing.Type[Attribute]] = dict()

    @staticmethod
    def add(attribute: typing.Type[Attribute]) -> typing.Type[Attribute]:
        CookbookAttributes.ATTRIBUTES.update({att_type: attribute for att_type in attribute.TYPES})
        return attribute  # return for Attribute's decorator

    @staticmethod
    def add_custom_attribute(cls: typing.Type[T]) -> None:
        from pyanhmi import CustomAttribute  # avoid circular import error
        CookbookAttributes.ATTRIBUTES[cls] = CustomAttribute

    @staticmethod
    def has(att_type: typing.Any) -> bool:
        return att_type in CookbookAttributes.ATTRIBUTES

    @staticmethod
    def get(value_type: typing.Any) -> Attribute:
        """
        :param value_type:
        :return: instance of Attribute's child. E.g: DictAttribute(value_type),...
        """
        return CookbookAttributes._get_attribute_instance(value_type)(value_type)

    @staticmethod
    def _get_attribute_instance(value_type: typing.Any) -> typing.Type[Attribute]:
        """
        :param value_type: can be hash(string) value
        :return:
        """
        if not value_type:
            return CookbookAttributes.ATTRIBUTES.get(typing.Any)

        result = CookbookAttributes.ATTRIBUTES.get(value_type)
        if result:
            return result

        origin_type = typing.get_origin(value_type)
        result = CookbookAttributes.ATTRIBUTES.get(origin_type)
        return result if result else CookbookAttributes.ATTRIBUTES.get(typing.Any)

    def get_user_define_modules(func):
        """
        See is_user_defined_type description
        :return:
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # Init Config.USER_DEFINE_MODULES. Only executed once
        Config.USER_DEFINE_MODULES = {module for module in Config.ROOT_DIRS if module not in Config.IGNORE_FOLDER}
        return wrapper

    @staticmethod
    @get_user_define_modules
    def is_user_defined_type(value_type) -> bool:
        """
        Check whether value_type is the type defined by user or not
        Example of not user-defined types: int, str, list
        :param value_type:
        :return:
        """
        return value_type.__module__.split(".")[0] in Config.USER_DEFINE_MODULES

    @staticmethod
    def get_user_defined_types(cls):
        """
        Return the set contain user-defined types of
        1. The class itself
        2. Class's Attributes
        :param cls:
        :return:
        """
        return {attribute_type for attribute_type in CookbookAttributes.get_attribute_types(cls)
                if CookbookAttributes.is_user_defined_type(attribute_type)}

    @staticmethod
    def get_attribute_types(cls: typing.Any) -> typing.Set[typing.Any]:
        """
        Retrieve user-defined types recursively
        :param cls:
        :return:
        """
        result = set()
        result.add(cls)
        try:
            child_types = typing.get_type_hints(cls)
            for att, att_type in child_types.items():
                result.add(att_type)
                for arg in typing.get_args(att_type):
                    result = result.union(CookbookAttributes.get_attribute_types(arg))
        except TypeError:
            pass
        try:
            nested_types = typing.get_args(cls)
            for att_type in nested_types:
                result = result.union(CookbookAttributes.get_attribute_types(att_type))
        except AttributeError:
            pass
        return result

