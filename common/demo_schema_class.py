import json
import random
import typing
from collections import defaultdict, OrderedDict
from collections.abc import Iterable
from datetime import datetime
from enum import Enum
from ipaddress import IPv4Address
from typing import Optional, Tuple, Dict, List, Any, Set, Union
from uuid import UUID

import pytest
from _decimal import Decimal

from MostOuterSchemaclass import OuterClass
from common.Config import Config, CastingMode, ExportOrder
from common.Error import InvalidDatatype, InvalidData
from common.NestedDirectory.NestNestedDirectory.nested_schemaclass import NestedClass
from common.schema_class import Product, ProductDescription, Product2, ConvertedProduct
from common.schema_classes_test import ClassicParent, AttributeTypesChild, Level4, AttributeTypesParent, StrClass, \
    IntClass, CompositeClass, FrozenSetDataclass, OrderedDictDataclass, StrDataclass, \
    IntDataclass, DictsDataclass, DictDataclass, DictClass, DictsClass, DictCompositeClass, DefaultDictDataclass, \
    NestedDefaultDictDataclass, DefaultDictsDataclass, SetDataclass, SetClass, SetsDataclass, ListDataclass, \
    TupleDataclass, TuplesDataclass, FrozenSetClass, FrozenSetsDataclass, UnionDataclass, UnionDataclass2, \
    FloatDataclass, BoolDataclass, StrictModeClass, SetFieldDirectly
from pyanhmi import BoolAttribute
from pyanhmi.Attributes.AnyAttribute import AnyAttribute
from pyanhmi.Attributes.DefaultDictAttribute import DefaultDictAttribute
from pyanhmi.Attributes.DictAttribute import DictAttribute
from pyanhmi.Attributes.ListAttribute import ListAttribute
from pyanhmi.Attributes.UnionAttribute import UnionAttribute
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create
from pyanhmi.LunchBox import LunchBox
from dataclasses import dataclass
from typing import ClassVar, Optional, Tuple

from pyanhmi.Field import Field
from pyanhmi.Recipe.Recipe import Recipe


@dataclass
class UserDb1:
    email: str
    name: str
    address: str = ""

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "email": Field(alias="user_email"),
            "name": Field(alias="user_name"),
        }
    )


@dataclass
class UserDb2:
    user_email: str
    full_name: str
    first_name: str = ""
    last_name: str = ""

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "full_name": Field(alias="user_name"),
        }
    )


@dataclass
class ReportUser:
    mail: str
    name: str
    first_name: str
    last_name: str
    address: str

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "mail": Field(alias="user_email"),
            "name": Field(alias="user_name"),
        }
    )


@dataclass
class NestedObj:
    nested: tuple


@dataclass
class OuterObj:
    outer: Optional[Tuple[Dict[str, Union[List[NestedObj], Set[int]]], typing.DefaultDict[str, int]]]
