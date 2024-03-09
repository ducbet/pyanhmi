from common.Config import Mode, Config
from common.schema_classes_test import StrClass, StrDataclass
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create

if __name__ == '__main__':
    CookbookRecipe.clear()
    Config.MODE = Mode.CASTING


    obj_dataclass = create({"val_1": 123}, StrDataclass)
    obj = create({"val_1": 123}, StrClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == "123"