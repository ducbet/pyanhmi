import inspect

from common.schema_classes_test import PydanticClass, SetFieldDirectly, user_validator, SetFieldParent, \
    ParentWithProperty, Level1
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.ObjectCreator import ObjectCreator

if __name__ == '__main__':
    data = {
        "val_1": 2,
        "val_2": {
            "val_2_2": 5
        },
    }
    obj = ObjectCreator.create_obj(data, SetFieldDirectly)
    print(CookbookRecipe.get(SetFieldDirectly).get_ingredient("val_1"))
    print(obj)

    # print(CookbookValidators.get_all())
    # obj = PydanticClass(**data)
    # print(type(obj), obj)


    # print(user_validator, user_validator.__qualname__)
    # print(SetFieldDirectly.val_1_validator, SetFieldDirectly.val_1_validator.__qualname__)
    # print(SetFieldParent.parent_validator, SetFieldParent.parent_validator.__qualname__)
    # print(Level1.lv1_method, Level1.lv1_method.__qualname__)
