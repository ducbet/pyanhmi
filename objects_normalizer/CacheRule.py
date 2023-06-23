import re
import typing

from objects_normalizer.Config import Config
from objects_normalizer.Field import NormalizeRule
from objects_normalizer.Attributes.AttributeManager import AttributeManager


class CacheRule:
    cached_classes = set()

    @staticmethod
    def get_instance_attributes(obj) -> typing.Set[str]:
        return set([attr for attr in obj.__dir__()
                    if attr != Config.normalize_rules_field_name and
                    attr != Config.normalize_rules_field_name_2 and
                    attr != Config.localize_rules_field_name and
                    not attr.startswith("_") and
                    not hasattr(obj.__getattribute__(attr), "__call__")])

    @staticmethod
    def _create_normalize_rules(obj):
        cls = type(obj)
        if hasattr(cls, Config.normalize_rules_field_name_2):
            return
        setattr(cls, Config.normalize_rules_field_name_2, {})
        CacheRule.cached_classes.add(cls)

        user_rules = getattr(cls, Config.normalize_rules_field_name, {})
        rules = getattr(cls, Config.normalize_rules_field_name_2)
        field_types = typing.get_type_hints(cls)
        # print(f"_create_normalize_rules obj: {obj}")
        for att in CacheRule.get_instance_attributes(obj):
            is_class_var = hasattr(cls, att)
            field_type = field_types.get(att, typing.Any)
            normalizable_fields = AttributeManager.get_user_defined_types(field_type)
            for normalizable_field in normalizable_fields:
                CacheRule.cache_rules(cls=normalizable_field)

            user__att_rule = user_rules.get(att)
            rule = NormalizeRule(name=att, attribute_type=field_type, is_class_var=is_class_var)
            rules[att] = rule
            if not user__att_rule:
                continue
            if not isinstance(user__att_rule, dict) and not isinstance(user__att_rule, str):
                raise TypeError("Field rule must be dict or string")

            if isinstance(user__att_rule, str):
                rule.alias = user__att_rule
                continue
            rule.alias = user__att_rule.get("name")
            rule.getter_func = user__att_rule.get("getter_func")

    @staticmethod
    def get_normalize_rule(target) -> dict:
        return getattr(target, Config.normalize_rules_field_name_2, {})

    @staticmethod
    def get_all_normalize_rules():
        return {cls: CacheRule.get_normalize_rule(cls) for cls in CacheRule.cached_classes}

    @staticmethod
    def _try_mock_obj(obj_type):
        try:
            return obj_type()
        except TypeError as e:
            err_msg = str(e)
            # __init__() missing 3 required positional arguments: 'param1', 'param2', and 'param3'
            if "__init__() missing" not in err_msg:
                raise e
            obj_params = {param: None for param in re.findall(r"'(.*?)'", err_msg)}
            return obj_type(**obj_params)

    @staticmethod
    def cache_rules(obj=None, cls=None):
        # print(f"cache_rules: obj: {obj}, cls: {cls}")
        # priority cls to get default value
        if not obj and not cls:
            return
        if not cls:
            cls = type(obj)
        obj = CacheRule._try_mock_obj(cls)

        CacheRule._create_normalize_rules(obj)
