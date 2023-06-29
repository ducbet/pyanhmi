from common.Config import Mode, Config
from common.schema_classes_test import DictDataclass, DictClass, SetFieldDirectly, StrictModeClass
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.ObjectCreator import ObjectCreator
from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe

if __name__ == '__main__':
    Config.MODE = Mode.STRICT

    recipe = AuthenticRecipe(cls=StrictModeClass)
    CookbookRecipe.add(recipe)


    assert CookbookRecipe.has(recipe)
    assert CookbookRecipe.has(StrictModeClass)
    assert CookbookRecipe.get(StrictModeClass) is not None

    val_1_ingredient = CookbookRecipe.get(StrictModeClass).get_ingredient("val_1")
    print(val_1_ingredient)
    # user defined recipe is override authentic recipe
    assert val_1_ingredient.mode == Mode.DUCK
    assert val_1_ingredient.alias == "val 1's alias"


