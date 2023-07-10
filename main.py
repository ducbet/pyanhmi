from common.Config import Mode, Config
from common.schema_classes_test import IntDataclass, FloatDataclass
from pyanhmi.Creator import create

if __name__ == '__main__':
    Config.MODE = Mode.CASTING

    obj_int, obj_float = create({"val_1": 123}, [IntDataclass, FloatDataclass])
    print(obj_int.val_1)
    print(obj_float.val_1)