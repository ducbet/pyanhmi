from collections import defaultdict
from dataclasses import dataclass
from typing import ClassVar, List, Final, FrozenSet, Optional, Tuple, Dict, Union, Set, Any, DefaultDict, OrderedDict, \
    Callable

from common.Config import Mode
from pyanhmi.Field import Field
from pyanhmi.Recipe.Recipe import Recipe


@dataclass
class Parent:
    parent_name: str


@dataclass
class Children(Parent):
    children_name: str


@dataclass
class ChildrenWithClassVar(Parent):
    class_var_children_name: ClassVar[str] = "class_var_children_name"


@dataclass
class ParentWithProperty:
    _parent_with_property_name: str

    @property
    def parent_with_property_name(self) -> str:
        return f"@property {self._parent_with_property_name}"

    @parent_with_property_name.setter
    def parent_with_property_name(self, name):
        self._parent_with_property_name = name


@dataclass
class ChildrenWithProperty(Parent):
    _children_with_property_name: str

    @property
    def children_with_property_name(self) -> str:
        return f"@property {self._children_with_property_name}"

    @children_with_property_name.setter
    def children_with_property_name(self, name):
        self._children_with_property_name = name


@dataclass
class ChildrenAndParentWithProperty(ParentWithProperty):
    _children_with_property_name: str

    @property
    def children_with_property_name(self) -> str:
        return f"@property {self._children_with_property_name}"

    @children_with_property_name.setter
    def children_with_property_name(self, name):
        self._children_with_property_name = name


class ClassicParent:
    def __init__(self, parent_name):
        self.parent_name = parent_name


class ClassicChildren(ClassicParent):
    def __init__(self, parent_name, children_name):
        super().__init__(parent_name)
        self.children_name = children_name


class ClassicChildrenWithClassVar(ClassicParent):
    class_var_children_name = "class_var_children_name"

    def __init__(self, parent_name):
        super().__init__(parent_name)


class ClassicParentWithProperty:
    def __init__(self, parent_name):
        self._parent_with_property_name = parent_name

    @property
    def parent_with_property_name(self) -> str:
        return f"@property {self._parent_with_property_name}"

    @parent_with_property_name.setter
    def parent_with_property_name(self, name):
        self._parent_with_property_name = name


class ClassicChildrenWithProperty(ClassicParent):
    def __init__(self, parent_name, children_name):
        super().__init__(parent_name)
        self._children_with_property_name = children_name

    @property
    def children_with_property_name(self) -> str:
        return f"@property {self._children_with_property_name}"

    @children_with_property_name.setter
    def children_with_property_name(self, name):
        self._children_with_property_name = name


class ClassicChildrenAndParentWithProperty(ClassicParentWithProperty):
    def __init__(self, parent_name, children_name):
        super().__init__(parent_name)
        self._children_with_property_name = children_name

    @property
    def children_with_property_name(self) -> str:
        return f"@property {self._children_with_property_name}"

    @children_with_property_name.setter
    def children_with_property_name(self, name):
        self._children_with_property_name = name


@dataclass
class Level1:
    _lv1_instance_att_1: str
    lv1_class_att_1: ClassVar[str] = "lv1_class_att_1"

    @property
    def lv1_instance_att_1(self) -> str:
        return f"@property {self._lv1_instance_att_1}"

    @lv1_instance_att_1.setter
    def lv1_instance_att_1(self, _lv1_instance_att_1):
        self._lv1_instance_att_1 = _lv1_instance_att_1

    def lv1_method(self):
        return


@dataclass
class Level2(Level1):
    _lv2_instance_att_1: str
    lv2_class_att_1: ClassVar[str] = "lv2_class_att_1"

    @property
    def lv2_instance_att_1(self) -> str:
        return f"@property {self._lv2_instance_att_1}"

    @lv2_instance_att_1.setter
    def lv2_instance_att_1(self, _lv2_instance_att_1):
        self._lv2_instance_att_1 = _lv2_instance_att_1


class Level3(Level2):
    lv3_class_att_1 = "lv3_class_att_1"

    def __init__(self, _lv1_instance_att_1, _lv2_instance_att_1, _lv3_instance_att_1):
        super().__init__(_lv1_instance_att_1, _lv2_instance_att_1)
        self._lv3_instance_att_1 = _lv3_instance_att_1

    @property
    def lv3_instance_att_1(self) -> str:
        return f"@property {self._lv3_instance_att_1}"

    @lv3_instance_att_1.setter
    def lv3_instance_att_1(self, _lv3_instance_att_1):
        self._lv3_instance_att_1 = _lv3_instance_att_1

    def lv3_method(self):
        return


class Level4(Level3):
    lv4_class_att_1 = "lv4_class_att_1"

    def __init__(self, _lv1_instance_att_1, _lv2_instance_att_1, _lv3_instance_att_1, _lv4_instance_att_1):
        super().__init__(_lv1_instance_att_1, _lv2_instance_att_1, _lv3_instance_att_1)
        self._lv4_instance_att_1 = _lv4_instance_att_1

    @property
    def lv4_instance_att_1(self) -> str:
        return f"@property {self._lv4_instance_att_1}"

    @lv4_instance_att_1.setter
    def lv4_instance_att_1(self, _lv4_instance_att_1):
        self._lv4_instance_att_1 = _lv4_instance_att_1


@dataclass
class AttributeTypesParent:
    a_tuple: tuple


@dataclass
# class AttributeTypesChild(AttributeTypesParent):
class AttributeTypesChild:
    a_Optional: Optional[Tuple[Dict[str, Union[List[AttributeTypesParent], Set[int]]], Any]]


@dataclass
class CompositeClass:
    composite: str


# class CompositeClass:
#     def __init__(self, composite: str):
#         self.composite = composite


@dataclass
class StrDataclass:
    val_1: str


class StrClass:
    def __init__(self, val_1: str):
        self.val_1 = val_1


@dataclass
class IntDataclass:
    val_1: int


class IntClass:
    def __init__(self, val_1: int):
        self.val_1 = val_1


@dataclass
class FloatDataclass:
    val_1: float


@dataclass
class BoolDataclass:
    val_1: bool


@dataclass
class DictDataclass:
    val_1: Dict[str, int]


class DictClass:
    def __init__(self, val_1: Dict[str, int]):
        self.val_1 = val_1


class DictCompositeClass:
    def __init__(self, val_1: Dict[str, IntClass]):
        self.val_1 = val_1


@dataclass
class DictsDataclass:
    val_1: dict
    val_2: Dict
    val_3: Dict[str, int]
    val_4: dict[int, str]


@dataclass
class DictsClass:
    def __init__(self, val_1: dict, val_2: Dict, val_3: Dict[str, int], val_4: dict[int, str]):
        self.val_1 = val_1
        self.val_2 = val_2
        self.val_3 = val_3
        self.val_4 = val_4


@dataclass
class DefaultDictDataclass:
    val_1: DefaultDict[str, list[int]]


@dataclass
class NestedDefaultDictDataclass:
    val_1: DefaultDict[str, DefaultDict[str, DefaultDict[str, list[int]]]]


@dataclass
class DefaultDictsDataclass:
    val_1: defaultdict[str, list[CompositeClass]]
    val_2: DefaultDict[str, list[int]]


class DefaultDictsClass:
    def __init__(self, val_1: defaultdict[str, list[CompositeClass]], val_2: DefaultDict[str, list[int]]):
        self.val_1 = val_1
        self.val_2 = val_2


@dataclass
class OrderedDictDataclass:
    val_1: OrderedDict[str, int]


class OrderedDictClass:
    def __init__(self, val_1: OrderedDict[str, int]):
        self.val_1 = val_1


@dataclass
class OrderedDictsDataclass:
    val_1: OrderedDict
    val_2: OrderedDict[str, int]


@dataclass
class SetDataclass:
    val_1: Set[str]


class SetClass:
    def __init__(self, val_1: Set[str]):
        self.val_1 = val_1


@dataclass
class SetsDataclass:
    val_1: set
    val_2: Set
    val_3: set[str]
    val_4: Set[int]


@dataclass
class FrozenSetDataclass:
    val_1: FrozenSet[str]


class FrozenSetClass:
    def __init__(self, val_1: FrozenSet[str]):
        self.val_1 = val_1


@dataclass
class FrozenSetsDataclass:
    val_1: FrozenSet
    val_2: frozenset
    val_3: FrozenSet[str]
    val_4: frozenset[int]


@dataclass
class ListDataclass:
    val_1: List[str]


@dataclass
class DictsClass:
    def __init__(self, val_1: dict, val_2: Dict, val_3: Dict[str, int], val_4: dict[int, str]):
        self.val_1 = val_1
        self.val_2 = val_2
        self.val_3 = val_3
        self.val_4 = val_4


@dataclass
class TupleDataclass:
    val_1: Tuple[str, Tuple[int, str, str]]


@dataclass
class TuplesDataclass:
    val_1: Tuple[str, Tuple[int, str, str]]
    val_2: tuple[str, int]
    val_3: tuple
    val_4: Tuple


@dataclass
class UnionDataclass:
    val_1: Optional[List[Union[int, CompositeClass, str]]]


@dataclass
class UnionDataclass2:
    val_1: Union[int, CompositeClass]


@dataclass
class AnyDataclass:
    val_1: Any
    val_2: any


class AnyClass:
    def __init__(self, val_1: Any, val_2: any):
        self.val_1 = val_1
        self.val_2 = val_2


@dataclass
class CallableDataclass:
    val_1: Callable


class CallableClass:
    def __init__(self, val_1: Callable):
        self.val_1 = val_1


@dataclass
class ClassVarDataclass:
    val_1: ClassVar[CompositeClass] = None
    val_2: ClassVar[int] = 13123


class ClassVarClass:
    val_1: ClassVar[CompositeClass]
    val_2: ClassVar[int] = 13123

    def __init__(self):
        pass


@dataclass
class FinalDataclass:
    val_1: Final[int] = 4


@dataclass
class StrictModeClass:
    val_1: int

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "val_1": Field(mode=Mode.DUCK, alias="val 1's alias")
        }
    )

def user_validator(val):
    return "asdwqe " + val


@dataclass
class SetFieldDirectly:
    val_1: int = Field(default=0, mode=Mode.DUCK)

    PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
        ingredients={
            "val_1": Field(default=5, mode=Mode.CASTING, validators=[
                "val_1_validator",
                user_validator
            ])
        }
    )

    def val_1_validator(self):
        return "modifed val_1"
