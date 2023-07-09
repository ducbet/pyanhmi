from common.Config import Mode, Config
from common.Error import InvalidDatatype
from common.schema_classes_test import ClassicParent
from pyanhmi.Creator import create

if __name__ == '__main__':
    Config.MODE = Mode.CASTING
    try:
        create({}, ClassicParent)
    except InvalidDatatype as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'parent_name'"
