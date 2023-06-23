import os
import typing

from pyanhmi.Config import Config


class AttributeManager:
    CACHED_ATTRIBUTES = {}


    @staticmethod
    def is_final_type(value_type):
        origin_type = typing.get_origin(value_type)
        if origin_type == typing.Final:
            return True
        return False

    @staticmethod
    def get_cached_attribute(value_type):
        if not value_type:
            return AttributeManager.CACHED_ATTRIBUTES.get(typing.Any)
        if hasattr(value_type, Config.PYANHMI_RECIPE):
            return AttributeManager.CACHED_ATTRIBUTES.get("CustomTypeAttribute")

        if value_type in AttributeManager.CACHED_ATTRIBUTES:
            return AttributeManager.CACHED_ATTRIBUTES[value_type]
        origin_type = typing.get_origin(value_type)

        result = AttributeManager.CACHED_ATTRIBUTES.get(origin_type)
        # print(f"get_TypeManager: value_type: {value_type}. origin_type: {origin_type}. result: {result}")
        return result if result else AttributeManager.CACHED_ATTRIBUTES.get(typing.Any)

    @staticmethod
    def is_user_defined_type(value_type):
        ignore_folder = ("test", "venv")
        user_define_modules = {module.split(".")[0] for module in os.listdir(Config.ROOT_PATH) if module[0] not in (".", "_") and module not in ignore_folder}
        return value_type.__module__.split(".")[0] in user_define_modules
        # return value_type.__module__ not in ("builtins", "typing", "ipaddress", "enum", "decimal", "uuid", "datetime")

    @staticmethod
    def get_user_defined_types(cls):
        # return [field for field in TypeCheckManager.get_field_types(cls) if _is_normalizable_fields(field)]
        return {attribute_type for attribute_type in AttributeManager.get_attribute_types(cls)
                if AttributeManager.is_user_defined_type(attribute_type)}

    @staticmethod
    def get_attribute_types(cls):
        result = set()
        result.add(cls)
        try:
            child_types = typing.get_type_hints(cls)
            for att, att_type in child_types.items():
                result.add(att_type)
                for arg in typing.get_args(att_type):
                    result = result.union(AttributeManager.get_attribute_types(arg))
        except TypeError:
            pass
        try:
            nested_types = typing.get_args(cls)
            for att_type in nested_types:
                result = result.union(AttributeManager.get_attribute_types(att_type))
        except AttributeError:
            pass
        return result
