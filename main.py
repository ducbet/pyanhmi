from common.Config import Mode, Config
from common.schema_classes_test import DictDataclass, DictClass
from pyanhmi.ObjectCreator import ObjectCreator

if __name__ == '__main__':
    Config.MODE = Mode.STRICT

    obj_dataclass = ObjectCreator.create_obj({"val_1": {"1": 2}}, DictDataclass)
    obj = ObjectCreator.create_obj({"val_1": {"1": 2}}, DictClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == {"1": 2}
