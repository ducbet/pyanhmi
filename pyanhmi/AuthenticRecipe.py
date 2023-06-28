import typing
from typing import Dict

from pyanhmi import AttributeManager
from pyanhmi.Config import Config
from pyanhmi.Cookbook import Cookbook
from pyanhmi.Field import Field
from pyanhmi.Helper import Helper
from pyanhmi.Recipe import Recipe


class AuthenticRecipe(Recipe):
    def __init__(self, cls=None, obj=None):
        if not obj and not cls:
            raise ValueError("Both obj and cls cannot be None")
        # prioritize cls to create a new object with minimal parameters
        if not cls:
            cls = type(obj)
        obj = Helper.try_mock_obj(cls)
        super().__init__(self._extract_ingredients(obj))
        self.based_on_cls = cls
        print("__init__", self.ingredients)
        self.update_user_defined_recipe()

    def update_user_defined_recipe(self):
        # prioritize user_defined_recipe inside class instead of automatically generated from type hint
        user_defined_recipe = getattr(self.based_on_cls, Config.PYANHMI_RECIPE, None)
        if not user_defined_recipe:
            return
        self.update(user_defined_recipe)
        print("update_user_defined_recipe", self.ingredients)

    @staticmethod
    def _extract_ingredients(obj):
        cls = type(obj)
        ingredients: Dict[str, Field] = {}

        field_types = cls.__init__.__annotations__
        # todo should have typing.get_type_hints(cls) to get class variable or not?
        for att in Recipe.get_instance_attributes(obj):
            attribute_type = field_types.get(att, typing.Any)

            for user_defined_type in AttributeManager.get_user_defined_types(attribute_type):
                Cookbook.add_recipe(AuthenticRecipe(cls=user_defined_type))

            ingredients[att] = Field(
                name=att,
                attribute_type=attribute_type,
                is_class_var=hasattr(cls, att)
            )
        return ingredients

    def __hash__(self):
        """
        Hash value is hash value of based_on_cls variable (in order to find recipe in set, dict)
        :return:
        """
        return self.get_hash(self.based_on_cls)

    def __repr__(self):
        return f"AuthenticRecipe(based_on_cls={self.based_on_cls}, ingredients={[self.ingredients.keys()]})"
