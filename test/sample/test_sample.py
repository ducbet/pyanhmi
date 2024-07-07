import pytest

from common.Config import Config, CastingMode
from common.schema_classes_test import StrDataclass, StrClass, IntDataclass, IntClass
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create


@pytest.fixture
def mode_casting():
    CookbookRecipe.clear()
    Config.MODE = CastingMode.CASTING
    print("            --mode_casting--")


def test_create_str_casting(mode_casting):
    obj_dataclass = create({"val_1": "123"}, StrDataclass)
    obj = create({"val_1": "123"}, StrClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == "123"

    obj_dataclass = create({"val_1": 123}, StrDataclass)
    obj = create({"val_1": 123}, StrClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == "123"


def test_create_int_casting(mode_casting):
    # CookbookRecipe.clear()
    # Config.MODE = Mode.CASTING

    obj_dataclass = create({"val_1": 123}, IntDataclass)
    obj = create({"val_1": 123}, IntClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj.val_1 == 123

    obj_dataclass = create({"val_1": "123"}, IntDataclass)
    obj = create({"val_1": "123"}, IntClass)
    assert obj_dataclass.__dict__ == obj.__dict__
    assert obj_dataclass.val_1 == 123
