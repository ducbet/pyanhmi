import re
import typing

from pyanhmi.Config import Config
from pyanhmi.Field import Field
from pyanhmi.AttributeManager import AttributeManager
from pyanhmi.Recipe import Recipe


class Cookbook:
    RECIPES = set()

    @staticmethod
    def get_instance_attributes(obj) -> typing.Set[str]:
        return set([attr for attr in obj.__dir__()
                    if attr != Config.PYANHMI_RECIPE and
                    not attr.startswith("_") and
                    not hasattr(obj.__getattribute__(attr), "__call__")])

    @staticmethod
    def is_recipe_completed(cls):
        if not hasattr(cls, Config.PYANHMI_RECIPE):
            return False
        return getattr(cls, Config.PYANHMI_RECIPE).is_completed

    @staticmethod
    def _create_blank_recipe(cls):
        recipe = Recipe()
        setattr(cls, Config.PYANHMI_RECIPE, recipe)
        return recipe

    @staticmethod
    def _prepare_recipe(cls):
        if hasattr(cls, Config.PYANHMI_RECIPE):
            # use in-complete recipe defined by user
            return getattr(cls, Config.PYANHMI_RECIPE)
        else:
            return Cookbook._create_blank_recipe(cls)

    @staticmethod
    def _create_recipe(obj):
        cls = type(obj)
        if Cookbook.is_recipe_completed(cls):
            return getattr(cls, Config.PYANHMI_RECIPE)
        recipe = Cookbook._prepare_recipe(cls)
        Cookbook.RECIPES.add(cls)
        recipe.is_completed = True

        field_types = cls.__init__.__annotations__
        # todo should have typing.get_type_hints(cls) to get class variable or not?
        for att in Cookbook.get_instance_attributes(obj):
            attribute_type = field_types.get(att, typing.Any)

            for user_defined_type in AttributeManager.get_user_defined_types(attribute_type):
                Cookbook.create_recipe(cls=user_defined_type)

            field = recipe.get_ingredient(att)
            if not field:
                field = Field()
                recipe.add_ingredient(att, field)
            field.name = att
            field.attribute_type = attribute_type
            field.is_class_var = hasattr(cls, att)
        return recipe

    @staticmethod
    def create_recipe(obj=None, cls=None):
        if not obj and not cls:
            return
        # prioritize cls to create a new object with minimal parameters
        if not cls:
            cls = type(obj)
        obj = Cookbook.try_mock_obj(cls)
        recipe = Cookbook._create_recipe(obj)
        return recipe

    @staticmethod
    def get_normalize_rule(target) -> dict:
        return getattr(target, Config.PYANHMI_RECIPE, {})

    @staticmethod
    def get_all_normalize_rules():
        return {cls: Cookbook.get_normalize_rule(cls) for cls in Cookbook.RECIPES}

    @staticmethod
    def try_mock_obj(obj_type):
        try:
            return obj_type()
        except TypeError as e:
            err_msg = str(e)
            # __init__() missing 3 required positional arguments: 'param1', 'param2', and 'param3'
            if "__init__() missing" not in err_msg:
                raise e
            obj_params = {param: None for param in re.findall(r"'(.*?)'", err_msg)}
            return obj_type(**obj_params)
