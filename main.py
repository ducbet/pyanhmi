from common.schema_class import PublicApi, PydanticPublicApi, PublicApiEntry
from common.schema_classes_test import SetFieldDirectly
from cpthon_code.cy_test import c_called_func
from pyanhmi.Helper import Helper
from pyanhmi.ObjectCreator import ObjectCreator


if __name__ == '__main__':
    data = {
        "val_1": 2
    }
    obj = ObjectCreator.create_obj(data, SetFieldDirectly)
    print(obj)