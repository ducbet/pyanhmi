from common.Config import Mode, Config
from common.schema_classes_test import StrClass, FloatDataclass
from pyanhmi import BoolAttribute, DictAttribute
from pyanhmi.Creator import create

if __name__ == '__main__':
    Config.MODE = Mode.CASTING

    data = {"val_1": 123}

    obj_str, float_obj = create(data, classes=[StrClass, FloatDataclass], mode=Mode.CASTING)
    print(obj_str.__dict__)
    print(float_obj)

