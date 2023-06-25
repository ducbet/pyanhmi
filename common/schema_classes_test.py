from dataclasses import dataclass
from typing import ClassVar, List, Final, FrozenSet, Optional, Tuple, Dict, Union, Set, Any, DefaultDict, OrderedDict, \
    Callable


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
class AttributeTypesComposite:
    a_List: List[AttributeTypesParent]


@dataclass
# class AttributeTypesChild(AttributeTypesParent):
class AttributeTypesChild:
    a_Optional: Optional[Tuple[Dict[str, Union[List[AttributeTypesParent], Set[int]]], Any]]


@dataclass
class AttDict:
    a_dict: dict

class AttDictClassic:
    def __init__(self, a_dict: dict):
        self.a_dict = a_dict

@dataclass
class AttAny:
    a_Any: Any
    a_Callable: Callable

@dataclass
class AttFrozenSet:
    a_FrozenSet: FrozenSet[int]
    a_FrozenSet_str: FrozenSet[str]

@dataclass
class AttDefaultDict:
    a_DefaultDict: DefaultDict[str, list[AttributeTypesComposite]]
    a_DefaultDict_int: DefaultDict[str, list[int]]

@dataclass
class AttOrderedDict:
    a_OrderedDict: OrderedDict[str, int]
    a_OrderedDict_list_tuple: OrderedDict[str, int]


@dataclass
class AttClassVar:
    a_dict: dict
    a_ClassVar: ClassVar[AttributeTypesComposite] = None
    a_ClassVar_2: ClassVar[int] = 13123
    a_Final: Final[int] = 4




@dataclass
class StrClass:
    id: str


@dataclass
class IntClass:
    id: int



