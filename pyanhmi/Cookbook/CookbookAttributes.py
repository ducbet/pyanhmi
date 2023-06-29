import os
import typing

from pyanhmi.Attributes.Attribute import Attribute
from common.Config import Config
from pyanhmi.Cookbook.Cookbook import Cookbook
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe


class CookbookAttributes(Cookbook):
    ATTRIBUTES: typing.Dict[typing.Union[str, typing.Type], Attribute] = dict()

    @staticmethod
    def add(attribute):
        CookbookAttributes.ATTRIBUTES.update({att_type: attribute for att_type in attribute.TYPES})
        return attribute  # return for Attribute's decorator

    @staticmethod
    def has(att_type):
        return att_type in CookbookAttributes.ATTRIBUTES

    @staticmethod
    def get(value_type):
        # todo should return instance???
        return CookbookAttributes.get_attribute_instance(value_type)(value_type)

    @staticmethod
    def get_attribute_instance(value_type):
        """
        :param value_type: can be hash(string) value
        :return:
        """
        if not value_type:
            return CookbookAttributes.ATTRIBUTES.get(typing.Any)
        if CookbookRecipe.has(value_type):
            return CookbookAttributes.get_attribute_instance(Config.CustomAttribute)

        if value_type in CookbookAttributes.ATTRIBUTES:
            return CookbookAttributes.ATTRIBUTES[value_type]
        origin_type = typing.get_origin(value_type)

        result = CookbookAttributes.ATTRIBUTES.get(origin_type)
        return result if result else CookbookAttributes.ATTRIBUTES.get(typing.Any)

    @staticmethod
    def get_all():
        return CookbookAttributes.ATTRIBUTES


    @staticmethod
    def is_user_defined_type(value_type):
        ignore_folder = ("test", "venv")
        user_define_modules = {module.split(".")[0] for module in os.listdir(Config.ROOT_PATH) if module[0] not in (".", "_") and module not in ignore_folder}
        return value_type.__module__.split(".")[0] in user_define_modules
        # return value_type.__module__ not in ("builtins", "typing", "ipaddress", "enum", "decimal", "uuid", "datetime")

    @staticmethod
    def get_user_defined_types(cls):
        # return [field for field in TypeCheckManager.get_field_types(cls) if _is_normalizable_fields(field)]
        return {attribute_type for attribute_type in CookbookAttributes.get_attribute_types(cls)
                if CookbookAttributes.is_user_defined_type(attribute_type)}

    @staticmethod
    def get_attribute_types(cls):
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

