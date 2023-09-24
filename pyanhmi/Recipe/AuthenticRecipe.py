import typing
from typing import Dict

from common.Config import Config, EmptyValue
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Field import Field
from pyanhmi.Helper import Helper
from pyanhmi.Recipe.Recipe import Recipe


class AuthenticRecipe(Recipe):
    def __init__(self, cls=None, obj=None):
        if not obj and not cls:
            raise ValueError("Both obj and cls cannot be None")
        # prioritize cls to create a new object with minimal parameters
        if not cls:
            cls = type(obj)
        obj = Helper.try_mock_obj(cls)
        CookbookAttributes.add_custom_attribute(cls)  # have to add CustomAttribute before creating ingredients
        super().__init__(self._extract_ingredients(obj), based_on_cls=cls)

    @staticmethod
    def _extract_ingredients(obj):
        cls = type(obj)
        ingredients: Dict[str, Field] = {}

        field_types = cls.__init__.__annotations__
        for att in Recipe.get_instance_attributes(obj):
            attribute_type = field_types.get(att, typing.Any)

            for user_defined_type in CookbookAttributes.get_user_defined_types(attribute_type):
                if not CookbookRecipe.has(cls):
                    CookbookRecipe.add(cls=user_defined_type)
            ingredients[att] = Field(
                name=att,
                attribute_type=attribute_type,
                is_class_var=hasattr(cls, att),
                based_on_cls=type(obj),
                default=getattr(obj, att, EmptyValue.FIELD)
            )
        return ingredients

    def __repr__(self):
        return f"AuthenticRecipe(based_on_cls={self.based_on_cls}, ingredients={list(self.ingredients.keys())})"
