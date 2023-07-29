from common.Config import Mode, Config
from common.schema_class import Product
from common.schema_classes_test import UnionDataclass, CompositeClass
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create
from pyanhmi.Recipe.Recipe import Recipe

if __name__ == '__main__':
    Config.MODE = Mode.STRICT

    data = {
        "val_1": [
            "1", 2, {"composite": "3"}
        ]
    }

    obj = create(data, UnionDataclass)
    obj_comp = obj.val_1[2]
    assert isinstance(obj_comp, CompositeClass)
    assert obj_comp.composite == "3"
    obj.val_1[2] = obj_comp.__dict__
    assert obj.val_1 == ["1", 2, {"composite": "3"}]



