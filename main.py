from common.schema_classes_test import SetFieldDirectly, PydanticClass
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

    assert obj.val_1 == "action_2(action_1(bounded_action_1(2)))"
    assert obj.parent_val == "parent_action(action_2(origin))"

