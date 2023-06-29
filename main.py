from common.Config import Mode, Config
from common.schema_classes_test import DictDataclass, DictClass, SetFieldDirectly
from pyanhmi.ObjectCreator import ObjectCreator

if __name__ == '__main__':
    Config.MODE = Mode.STRICT

    a = SetFieldDirectly()
    print(a)
