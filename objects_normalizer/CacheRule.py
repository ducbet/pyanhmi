import re
import typing

from objects_normalizer.Config import Config
from objects_normalizer.NormalizeRule import NormalizeRule
from objects_normalizer.TypeCheckManager import TypeCheckManager


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

    # @staticmethod
    # def get_normalizable_fields(cls):
    #
    #     # if cls in ObjectsNormalizer.cached_classes:
    #     #     normalize_rules = getattr(cls, Config.normalize_rules_field_name)
    #     #     # print(f"get_normalizable_fields: {normalize_rules}")
    #     #     return {att: rule["composite"] for att, rule in normalize_rules.items() if rule.get("composite")}
    #     return TypeCheckManager.get_field_types(cls)
    #     # result = {}
    #     # for field, field_types in TypeCheckManager.get_field_types(cls).items():
    #     #     for field_type in field_types:
    #     #         if _is_normalizable_fields(field_type):
    #     #             result[field] = field_types[0]
    #     #             break
    #     # return result
    #     # return

    @staticmethod
    def _create_normalize_rules(obj):
        cls = type(obj)
        if hasattr(cls, Config.normalize_rules_field_name_2):
            return
        setattr(cls, Config.normalize_rules_field_name_2, {})
        rules = getattr(cls, Config.normalize_rules_field_name_2)
        field_types = typing.get_type_hints(cls)
        print(f"_create_normalize_rules obj: {obj}")
        for att in CacheRule.get_instance_attributes(obj):
            field_type = field_types.get(att, typing.Any)
            normalizable_fields = TypeCheckManager.get_normalizable_fields(field_type)
            for normalizable_field in normalizable_fields:
                CacheRule.cache_rules(cls=normalizable_field)

            if att not in rules:
                # print(f"att not in rules. att: {att}. field_type: {field_type}. rules: {rules}")
                rules[att] = NormalizeRule(localized_field_name=att, field_type=field_type)
                continue
            # re-format rule
            if isinstance(rules[att], str):
                rules[att] = NormalizeRule(localized_field_name=att, field_type=field_type, normalized_field_name=rules[att])
                continue

            rules[att] = NormalizeRule(localized_field_name=att,
                                       field_type=field_type,
                                       normalized_field_name=rules[att]["name"],
                                       getter_func_name=rules[att]["getter_func"])

    # @staticmethod
    # def _create_localize_rules(obj):
    #     cls = type(obj)
    #     normalize_rules: typing.Dict[str, NormalizeRule] = getattr(cls, Config.normalize_rules_field_name)
    #     localize_rules = {}
    #     for local_field, normalize_rule in normalize_rules.items():
    #         # print(f"local_field: {local_field}, normalize_rule: {normalize_rule}")
    #         localize_rules[normalize_rule.normalized_field_name] = NormalizeRule(localized_field_name=local_field)
    #     setattr(cls, Config.localize_rules_field_name, localize_rules)


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
        # if not obj:
        #     obj = CacheRule._try_mock_obj(cls)
        if not cls:
            cls = type(obj)
        obj = CacheRule._try_mock_obj(cls)

        CacheRule._create_normalize_rules(obj)
        CacheRule.cached_classes.add(type(obj))  # try to not go into infinite for loop


        # ObjectsNormalizer._create_localize_rules(obj)
