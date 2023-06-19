import re

from objects_normalizer.CacheRule import CacheRule
from objects_normalizer.Config import Config


class ObjectCreator:



    @staticmethod
    def _try_create_obj(obj_type, obj_params: dict = None):
        """
        There are two solutions:
        1. Call obj_type() and retrieving all required arguments
            - Can initialize mock instance (no params required)
            - Optional arguments can be ignored
        2. Call obj_type with all possible arguments and removing redundant arguments until can init instance successful
        :param obj_type:
        :param obj_params: Use solution 1 if None else solution 2
        :return:
        """
        if not obj_params:
            obj = CacheRule._try_mock_obj(obj_type)
            return obj
        for num_try in range(len(obj_params)):
            try:
                return obj_type(**obj_params)
            except TypeError as e:
                # redundant_key will raise error: __init__() got an unexpected keyword argument 'redundant_key'
                # -> remove redundant_key from obj_params until success
                err_msg = str(e)
                if "__init__() got an unexpected keyword argument " not in err_msg:
                    raise e
                redundant_key = err_msg \
                    .replace("__init__() got an unexpected keyword argument ", "") \
                    .replace("'", "")
                obj_params = {k: v for k, v in obj_params.items() if k != redundant_key}
        return obj_type()  # will raise error: TypeError: __init__() missing 1 required positional argument...

    @staticmethod
    def create_obj(obj_params: dict, obj_type):
        """

        :param obj_params:
        :param obj_type:
        :return:
        """
        # print(f"create_obj: obj_type: {obj_type}, {obj_params}")
        if not hasattr(obj_type, Config.normalize_rules_field_name_2):
        # if obj_type not in CacheRule.cached_classes:
            # obj = ObjectCreator._try_create_obj(obj_type, obj_params)
            CacheRule.cache_rules(cls=obj_type)

        # obj_type is cached
        normalize_rules = getattr(obj_type, Config.normalize_rules_field_name_2)
        print(f"normalize_rules: {normalize_rules}")
        # print(f"create_obj: normalize_rules: {normalize_rules.keys()}")
        # obj_params = {k: v for k, v in obj_params.items() if k in normalize_rules}
        params = {}
        for param, obj_param in obj_params.items():
            if param not in normalize_rules:
                continue
            if normalize_rules[param].is_final_att:
                continue
            print(f"create_obj: param {param}")
            # print(f"create_obj: normalize_rules[param]: {normalize_rules[param]}")
            params[param] = normalize_rules[param].create(obj_param)
        # print(f"create_obj: obj_type: {obj_type}, {params}")
        return obj_type(**params)
