import typing

from objects_normalizer.Config import Config


class TypeCheckManager:
    SUPPORT_TYPES = {}

    @staticmethod
    def is_normalizable_fields(value_type):
        return value_type.__module__ not in ("builtins", "typing")

    @staticmethod
    def get_TypeManager(value_type):
        if not value_type:
            return TypeCheckManager.SUPPORT_TYPES.get(typing.Any)
        if hasattr(value_type, Config.normalize_rules_field_name_2):
            return TypeCheckManager.SUPPORT_TYPES.get("CustomTypeAttribute")

        if value_type in TypeCheckManager.SUPPORT_TYPES:
            return TypeCheckManager.SUPPORT_TYPES[value_type]
        origin_type = typing.get_origin(value_type)
        # print(f"get_TypeManager: value_type: {value_type}. origin_type: {origin_type}")

        result = TypeCheckManager.SUPPORT_TYPES.get(origin_type)
        return result if result else TypeCheckManager.SUPPORT_TYPES.get(typing.Any)

    @staticmethod
    def get_normalizable_fields(cls):
        def _is_normalizable_fields(c):
            # note https://docs.python.org/3/library/collections.html
            return c.__module__ not in ("builtins", "typing")

        # return [field for field in TypeCheckManager.get_field_types(cls) if _is_normalizable_fields(field)]
        return {field for field in TypeCheckManager.get_field_types(cls) if _is_normalizable_fields(field)}

    @staticmethod
    def get_field_types(cls):
        result = set()
        result.add(cls)
        try:
            child_types = typing.get_type_hints(cls)
            for att, att_type in child_types.items():
                result.add(att_type)
                for arg in typing.get_args(att_type):
                    result = result.union(TypeCheckManager.get_field_types(arg))
        except TypeError:
            pass
        try:
            nested_types = typing.get_args(cls)
            for att_type in nested_types:
                result = result.union(TypeCheckManager.get_field_types(att_type))
        except AttributeError:
            pass
        return result
