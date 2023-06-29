import re


class Helper:
    @staticmethod
    def try_mock_obj(obj_type):
        try:
            tmp = obj_type()
            # print(f"try_mock_obj can create {obj_type} without params")
            return tmp
        except TypeError as e:
            err_msg = str(e)
            # print(f"try_mock_obj err_msg: {err_msg}")
            # __init__() missing 3 required positional arguments: 'param1', 'param2', and 'param3'
            if "__init__() missing" not in err_msg:
                raise e
            obj_params = {param: None for param in re.findall(r"'(.*?)'", err_msg)}
            return obj_type(**obj_params)

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
            obj = Helper.try_mock_obj(obj_type)
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
