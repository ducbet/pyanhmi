# content of test_sample.py
import inspect
from pprint import pprint

from common.schema_classes_test import Children, Parent, ChildrenWithClassVar, ChildrenWithProperty, ParentWithProperty, \
    ChildrenAndParentWithProperty, ClassicParent, ClassicChildren, ClassicChildrenWithClassVar, \
    ClassicParentWithProperty, ClassicChildrenWithProperty, ClassicChildrenAndParentWithProperty, Level4


def test_dataclass():
    expect_result = {'parent_name': "parent_name"}
    obj = Parent(parent_name="parent_name")
    print()

    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': "parent_name"}

    # print(f"obj.__annotations__: {obj.__annotations__}")  # obj.__annotations__: {'parent_name': <class 'int'>}

     #    ("obj.__dir__(): ['parent_name', '__module__', '__annotations__', '__dict__', "
     # "'__weakref__', '__doc__', '__dataclass_params__', '__dataclass_fields__', "
     # "'__init__', '__repr__', '__eq__', '__hash__', '__str__', '__getattribute__', "
     # "'__setattr__', '__delattr__', '__lt__', '__le__', '__ne__', '__gt__', "
     # "'__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', "
     # "'__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'parent_name': 'parent_name'}"

    # type(obj).__dict__: {
    #     '__annotations__': {'parent_name': <class 'int'>},
    #     '__doc__': 'Parent(parent_name: int)',
    #     '__dataclass_fields__': {'parent_name': ...
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # print(f"type(obj).__annotations__: {type(obj).__annotations__}")  # type(obj).__annotations__: {'parent_name': <class 'int'>}
     #     ("vars(type(obj)): {'__module__': 'common.schema_class', '__annotations__': "
     # "{'parent_name': <class 'str'>}, '__dict__': <attribute '__dict__' of "
     # "'Parent' objects>, '__weakref__': <attribute '__weakref__' of 'Parent' "
     # "objects>, '__doc__': 'Parent(parent_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x0000023EDACD40D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x0000023EDACD40D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x0000023EDD755940>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x0000023EDD7558B0>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x0000023EDD755B80>, '__hash__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")


     #    ("inspect.getmembers(type(obj)): [('__annotations__', {'parent_name': <class "
     # "'str'>}), ('__class__', <class 'type'>), ('__dataclass_fields__', "
     # "{'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x0000028F6AE330D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x0000028F6AE330D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}), '
     # "('__dataclass_params__', "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)), '
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__annotations__': {'parent_name': <class 'str'>}, '__dict__': <attribute "
     # "'__dict__' of 'Parent' objects>, '__weakref__': <attribute '__weakref__' of "
     # "'Parent' objects>, '__doc__': 'Parent(parent_name: str)', "
     # "'__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x0000028F6AE330D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x0000028F6AE330D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x0000028F6D8F6430>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x0000028F6D8F6310>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x0000028F6D8F65E0>, '__hash__': None})), ('__dir__', <method '__dir__' of "
     # "'object' objects>), ('__doc__', 'Parent(parent_name: str)'), ('__eq__', "
     # '<function __create_fn__.<locals>.__eq__ at 0x0000028F6D8F65E0>), '
     # "('__format__', <method '__format__' of 'object' objects>), ('__ge__', <slot "
     # "wrapper '__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', None), ('__init__', <function "
     # '__create_fn__.<locals>.__init__ at 0x0000028F6D8F6430>), '
     # "('__init_subclass__', <built-in method __init_subclass__ of type object at "
     # "0x0000028F6B9A8CE0>), ('__le__', <slot wrapper '__le__' of 'object' "
     # "objects>), ('__lt__', <slot wrapper '__lt__' of 'object' objects>), "
     # "('__module__', 'common.schema_classes_test'), ('__ne__', <slot wrapper "
     # "'__ne__' of 'object' objects>), ('__new__', <built-in method __new__ of type "
     # "object at 0x00007FFFA22B4E00>), ('__reduce__', <method '__reduce__' of "
     # "'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' "
     # "objects>), ('__repr__', <function __create_fn__.<locals>.__repr__ at "
     # "0x0000028F6D8F6310>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x0000028F6B9A8CE0>), ('__weakref__', <attribute '__weakref__' of 'Parent' "
     # 'objects>)]')
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")
    # assert obj.__dict__ == expect_result

    # type(obj).__init__().__annotations__: {'parent_name': <class 'str'>, 'return': None}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_dataclass_inherit():
    expect_result = {'parent_name': "parent_name", 'children_name': "children_name"}
    obj = Children(parent_name="parent_name", children_name="children_name")
    print()
    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': "parent_name", 'children_name': "children_name"}

    # print(f"obj.__annotations__: {obj.__annotations__}")  # obj.__annotations__: {'children_name': <class 'int'>}

     #    ("obj.__dir__(): ['parent_name', 'children_name', '__module__', "
     # "'__annotations__', '__doc__', '__dataclass_params__', "
     # "'__dataclass_fields__', '__init__', '__repr__', '__eq__', '__hash__', "
     # "'__dict__', '__weakref__', '__str__', '__getattribute__', '__setattr__', "
     # "'__delattr__', '__lt__', '__le__', '__ne__', '__gt__', '__ge__', '__new__', "
     # "'__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', "
     # "'__format__', '__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'parent_name': 'parent_name', 'children_name': 'children_name'}"

    # type(obj).__dict__: {
    #     '__annotations__': {'children_name': <class 'int'>},
    #     '__doc__': 'Children(parent_name: int, children_name: int)',
    #     '__dataclass_fields__': {'parent_name': Field(name='parent_name',...,
    #                            'children_name': Field(name='children_name',...,
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # print(f"type(obj).__annotations__: {type(obj).__annotations__}")  # type(obj).__annotations__: {'children_name': <class 'int'>}

     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__annotations__': "
     # "{'children_name': <class 'str'>}, '__doc__': 'Children(parent_name: str, "
     # "children_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x000001E0174240D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x000001E0174240D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'children_name': Field(name='children_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x000001E0174240D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x000001E0174240D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x000001E019EE5D30>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x000001E019EE5CA0>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x000001E019EE5EE0>, '__hash__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

    # ("inspect.getmembers(type(obj)): [('__annotations__', {'children_name': <class "
    #  "'str'>}), ('__class__', <class 'type'>), ('__dataclass_fields__', "
    #  "{'parent_name': Field(name='parent_name',type=<class "
    #  "'str'>,default=<dataclasses._MISSING_TYPE object at "
    #  '0x00000223CEE240D0>,default_factory=<dataclasses._MISSING_TYPE object at '
    #  '0x00000223CEE240D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
    #  "'children_name': Field(name='children_name',type=<class "
    #  "'str'>,default=<dataclasses._MISSING_TYPE object at "
    #  '0x00000223CEE240D0>,default_factory=<dataclasses._MISSING_TYPE object at '
    #  '0x00000223CEE240D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}), '
    #  "('__dataclass_params__', "
    #  '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)), '
    #  "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
    #  "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
    #  "'__annotations__': {'children_name': <class 'str'>}, '__doc__': "
    #  "'Children(parent_name: str, children_name: str)', '__dataclass_params__': "
    #  '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
    #  "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
    #  "'str'>,default=<dataclasses._MISSING_TYPE object at "
    #  '0x00000223CEE240D0>,default_factory=<dataclasses._MISSING_TYPE object at '
    #  '0x00000223CEE240D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
    #  "'children_name': Field(name='children_name',type=<class "
    #  "'str'>,default=<dataclasses._MISSING_TYPE object at "
    #  '0x00000223CEE240D0>,default_factory=<dataclasses._MISSING_TYPE object at '
    #  '0x00000223CEE240D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
    #  "'__init__': <function __create_fn__.<locals>.__init__ at "
    #  "0x00000223D18E6700>, '__repr__': <function __create_fn__.<locals>.__repr__ "
    #  "at 0x00000223D18E6670>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
    #  "0x00000223D18E68B0>, '__hash__': None})), ('__dir__', <method '__dir__' of "
    #  "'object' objects>), ('__doc__', 'Children(parent_name: str, children_name: "
    #  "str)'), ('__eq__', <function __create_fn__.<locals>.__eq__ at "
    #  "0x00000223D18E68B0>), ('__format__', <method '__format__' of 'object' "
    #  "objects>), ('__ge__', <slot wrapper '__ge__' of 'object' objects>), "
    #  "('__getattribute__', <slot wrapper '__getattribute__' of 'object' objects>), "
    #  "('__gt__', <slot wrapper '__gt__' of 'object' objects>), ('__hash__', None), "
    #  "('__init__', <function __create_fn__.<locals>.__init__ at "
    #  "0x00000223D18E6700>), ('__init_subclass__', <built-in method "
    #  "__init_subclass__ of type object at 0x00000223CF9028F0>), ('__le__', <slot "
    #  "wrapper '__le__' of 'object' objects>), ('__lt__', <slot wrapper '__lt__' of "
    #  "'object' objects>), ('__module__', 'common.schema_classes_test'), ('__ne__', "
    #  "<slot wrapper '__ne__' of 'object' objects>), ('__new__', <built-in method "
    #  "__new__ of type object at 0x00007FFFA22B4E00>), ('__reduce__', <method "
    #  "'__reduce__' of 'object' objects>), ('__reduce_ex__', <method "
    #  "'__reduce_ex__' of 'object' objects>), ('__repr__', <function "
    #  "__create_fn__.<locals>.__repr__ at 0x00000223D18E6670>), ('__setattr__', "
    #  "<slot wrapper '__setattr__' of 'object' objects>), ('__sizeof__', <method "
    #  "'__sizeof__' of 'object' objects>), ('__str__', <slot wrapper '__str__' of "
    #  "'object' objects>), ('__subclasshook__', <built-in method __subclasshook__ "
    #  "of type object at 0x00000223CF9028F0>), ('__weakref__', <attribute "
    #  "'__weakref__' of 'Parent' objects>)]")
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {'parent_name': <class 'str'>, 'children_name': <class 'str'>, 'return': None}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_dataclass_class_var():
    expect_result = {'parent_name': "parent_name", 'class_var_children_name': "class_var_children_name"}
    obj = ChildrenWithClassVar(parent_name="parent_name")
    print()
    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': "parent_name"}

    # print(f"obj.__annotations__: {obj.__annotations__}")  # obj.__annotations__: {'class_var_children_name': typing.ClassVar[str]}

     #    ("obj.__dir__(): ['parent_name', '__module__', '__annotations__', "
     # "'class_var_children_name', '__doc__', '__dataclass_params__', "
     # "'__dataclass_fields__', '__init__', '__repr__', '__eq__', '__hash__', "
     # "'__dict__', '__weakref__', '__str__', '__getattribute__', '__setattr__', "
     # "'__delattr__', '__lt__', '__le__', '__ne__', '__gt__', '__ge__', '__new__', "
     # "'__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', "
     # "'__format__', '__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'parent_name': 'parent_name'}"

    # type(obj).__dict__:{'__annotations__': {'class_var_children_name': typing.ClassVar[str]},
    #                     'class_var_children_name': "class_var_children_name",
    #                     '__doc__': 'ChildrenWithClassVar(parent_name: str)',
    #                     '__dataclass_fields__':
    #                         {'parent_name': ...,
    #                          'class_var_children_name': ...
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # print(f"type(obj).__annotations__: {type(obj).__annotations__}")  # type(obj).__annotations__: {'class_var_children_name': typing.ClassVar[str]}

     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__annotations__': "
     # "{'class_var_children_name': typing.ClassVar[str]}, "
     # "'class_var_children_name': 'class_var_children_name', '__doc__': "
     # "'ChildrenWithClassVar(parent_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x0000024513CE40D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x0000024513CE40D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'class_var_children_name': "
     # "Field(name='class_var_children_name',type=typing.ClassVar[str],default='class_var_children_name',default_factory=<dataclasses._MISSING_TYPE "
     # 'object at '
     # '0x0000024513CE40D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD_CLASSVAR)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x0000024516764E50>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x0000024516764DC0>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x00000245167670D0>, '__hash__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

     #    ("inspect.getmembers(type(obj)): [('__annotations__', "
     # "{'class_var_children_name': typing.ClassVar[str]}), ('__class__', <class "
     # "'type'>), ('__dataclass_fields__', {'parent_name': "
     # "Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000216AC3C40D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000216AC3C40D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'class_var_children_name': "
     # "Field(name='class_var_children_name',type=typing.ClassVar[str],default='class_var_children_name',default_factory=<dataclasses._MISSING_TYPE "
     # 'object at '
     # '0x00000216AC3C40D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD_CLASSVAR)}), '
     # "('__dataclass_params__', "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)), '
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__annotations__': {'class_var_children_name': typing.ClassVar[str]}, "
     # "'class_var_children_name': 'class_var_children_name', '__doc__': "
     # "'ChildrenWithClassVar(parent_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000216AC3C40D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000216AC3C40D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'class_var_children_name': "
     # "Field(name='class_var_children_name',type=typing.ClassVar[str],default='class_var_children_name',default_factory=<dataclasses._MISSING_TYPE "
     # 'object at '
     # '0x00000216AC3C40D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD_CLASSVAR)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x00000216AEE85820>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x00000216AEE85790>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x00000216AEE85A60>, '__hash__': None})), ('__dir__', <method '__dir__' of "
     # "'object' objects>), ('__doc__', 'ChildrenWithClassVar(parent_name: str)'), "
     # "('__eq__', <function __create_fn__.<locals>.__eq__ at 0x00000216AEE85A60>), "
     # "('__format__', <method '__format__' of 'object' objects>), ('__ge__', <slot "
     # "wrapper '__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', None), ('__init__', <function "
     # '__create_fn__.<locals>.__init__ at 0x00000216AEE85820>), '
     # "('__init_subclass__', <built-in method __init_subclass__ of type object at "
     # "0x00000216ACD6FF90>), ('__le__', <slot wrapper '__le__' of 'object' "
     # "objects>), ('__lt__', <slot wrapper '__lt__' of 'object' objects>), "
     # "('__module__', 'common.schema_classes_test'), ('__ne__', <slot wrapper "
     # "'__ne__' of 'object' objects>), ('__new__', <built-in method __new__ of type "
     # "object at 0x00007FFFA22B4E00>), ('__reduce__', <method '__reduce__' of "
     # "'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' "
     # "objects>), ('__repr__', <function __create_fn__.<locals>.__repr__ at "
     # "0x00000216AEE85790>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x00000216ACD6FF90>), ('__weakref__', <attribute '__weakref__' of 'Parent' "
     # "objects>), ('class_var_children_name', 'class_var_children_name')]")
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {'parent_name': <class 'str'>, 'return': None}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")

def test_dataclass_property():
    obj = ParentWithProperty(_parent_with_property_name="parent name")
    print()
    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'_parent_with_property_name': 'init name'}

    # print(f"obj.__annotations__: {obj.__annotations__}")  # obj.__annotations__: {'_parent_with_property_name': <class 'str'>}

     #    ("obj.__dir__(): ['_parent_with_property_name', '__module__', "
     # "'__annotations__', 'parent_with_property_name', '__dict__', '__weakref__', "
     # "'__doc__', '__dataclass_params__', '__dataclass_fields__', '__init__', "
     # "'__repr__', '__eq__', '__hash__', '__str__', '__getattribute__', "
     # "'__setattr__', '__delattr__', '__lt__', '__le__', '__ne__', '__gt__', "
     # "'__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', "
     # "'__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'_parent_with_property_name': 'parent name'}"

    # type(obj).__dict__: {
    #     '__module__': 'common.schema_class',
    #     '__annotations__': {'_parent_with_property_name': <class 'str'>},
    # 'parent_with_property_name': <property object at 0x000002BB0E8A9590>,
    # '__dict__': <attribute '__dict__' of 'ParentWithProperty' objects>,
    # '__doc__': 'ParentWithProperty(_parent_with_property_name: str)',
    # '__dataclass_fields__': {'_parent_with_property_name': ...
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # print(f"type(obj).__annotations__: {type(obj).__annotations__}")  # type(obj).__annotations__: {'_parent_with_property_name': <class 'str'>}

     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__annotations__': "
     # "{'_parent_with_property_name': <class 'str'>}, 'parent_with_property_name': "
     # "<property object at 0x0000023BC975F6D0>, '__dict__': <attribute '__dict__' "
     # "of 'ParentWithProperty' objects>, '__weakref__': <attribute '__weakref__' of "
     # "'ParentWithProperty' objects>, '__doc__': "
     # "'ParentWithProperty(_parent_with_property_name: str)', "
     # "'__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'_parent_with_property_name': "
     # "Field(name='_parent_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x0000023BC6C840D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x0000023BC6C840D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x0000023BC9758310>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x0000023BC9758280>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x0000023BC9758430>, '__hash__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")


     #    ("inspect.getmembers(type(obj)): [('__annotations__', "
     # "{'_parent_with_property_name': <class 'str'>}), ('__class__', <class "
     # "'type'>), ('__dataclass_fields__', {'_parent_with_property_name': "
     # "Field(name='_parent_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000213B9BC30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000213B9BC30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}), '
     # "('__dataclass_params__', "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)), '
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__annotations__': {'_parent_with_property_name': <class 'str'>}, "
     # "'parent_with_property_name': <property object at 0x00000213BC69E400>, "
     # "'__dict__': <attribute '__dict__' of 'ParentWithProperty' objects>, "
     # "'__weakref__': <attribute '__weakref__' of 'ParentWithProperty' objects>, "
     # "'__doc__': 'ParentWithProperty(_parent_with_property_name: str)', "
     # "'__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'_parent_with_property_name': "
     # "Field(name='_parent_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000213B9BC30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000213B9BC30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x00000213BC676CA0>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x00000213BC676C10>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x00000213BC676DC0>, '__hash__': None})), ('__dir__', <method '__dir__' of "
     # "'object' objects>), ('__doc__', "
     # "'ParentWithProperty(_parent_with_property_name: str)'), ('__eq__', <function "
     # "__create_fn__.<locals>.__eq__ at 0x00000213BC676DC0>), ('__format__', "
     # "<method '__format__' of 'object' objects>), ('__ge__', <slot wrapper "
     # "'__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', None), ('__init__', <function "
     # '__create_fn__.<locals>.__init__ at 0x00000213BC676CA0>), '
     # "('__init_subclass__', <built-in method __init_subclass__ of type object at "
     # "0x00000213BA63AF70>), ('__le__', <slot wrapper '__le__' of 'object' "
     # "objects>), ('__lt__', <slot wrapper '__lt__' of 'object' objects>), "
     # "('__module__', 'common.schema_classes_test'), ('__ne__', <slot wrapper "
     # "'__ne__' of 'object' objects>), ('__new__', <built-in method __new__ of type "
     # "object at 0x00007FFFA22B4E00>), ('__reduce__', <method '__reduce__' of "
     # "'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' "
     # "objects>), ('__repr__', <function __create_fn__.<locals>.__repr__ at "
     # "0x00000213BC676C10>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x00000213BA63AF70>), ('__weakref__', <attribute '__weakref__' of "
     # "'ParentWithProperty' objects>), ('parent_with_property_name', <property "
     # 'object at 0x00000213BC69E400>)]')
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {'_parent_with_property_name': <class 'str'>, 'return': None}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_dataclass_property2():
    obj = ChildrenWithProperty(parent_name="parent_name", _children_with_property_name="child name")
    print()
    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': 'parent_name', '_children_with_property_name': 'child name'}

    # print(f"obj.__annotations__: {obj.__annotations__}")  # obj.__annotations__: {'_children_with_property_name': <class 'str'>}

     #    ("obj.__dir__(): ['parent_name', '_children_with_property_name', '__module__', "
     # "'__annotations__', 'children_with_property_name', '__doc__', "
     # "'__dataclass_params__', '__dataclass_fields__', '__init__', '__repr__', "
     # "'__eq__', '__hash__', '__dict__', '__weakref__', '__str__', "
     # "'__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', "
     # "'__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', "
     # "'__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', "
     # "'__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # ("vars(obj): {'parent_name': 'parent_name', '_children_with_property_name': ""'child name'}")

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      '__annotations__': {'_children_with_property_name': <class 'str'>},
    # 'children_with_property_name': <property object at 0x000001BD6E9119F0>,
    # '__doc__': 'ChildrenWithProperty(parent_name: str, _children_with_property_name: str)',
    # '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False),
    # '__dataclass_fields__': {'parent_name': ...
    #                         '_children_with_property_name': ...
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # print(f"type(obj).__annotations__: {type(obj).__annotations__}")  # type(obj).__annotations__: {'_children_with_property_name': <class 'str'>}

     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__annotations__': "
     # "{'_children_with_property_name': <class 'str'>}, "
     # "'children_with_property_name': <property object at 0x0000026089EE6D10>, "
     # "'__doc__': 'ChildrenWithProperty(parent_name: str, "
     # "_children_with_property_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000260874130D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000260874130D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'_children_with_property_name': "
     # "Field(name='_children_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000260874130D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000260874130D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x0000026089ED6670>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x0000026089ED65E0>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x0000026089ED6790>, '__hash__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

     #    ("inspect.getmembers(type(obj)): [('__annotations__', "
     # "{'_children_with_property_name': <class 'str'>}), ('__class__', <class "
     # "'type'>), ('__dataclass_fields__', {'parent_name': "
     # "Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000235822A30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000235822A30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'_children_with_property_name': "
     # "Field(name='_children_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000235822A30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000235822A30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}), '
     # "('__dataclass_params__', "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)), '
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__annotations__': {'_children_with_property_name': <class 'str'>}, "
     # "'children_with_property_name': <property object at 0x0000023584D48EF0>, "
     # "'__doc__': 'ChildrenWithProperty(parent_name: str, "
     # "_children_with_property_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'parent_name': Field(name='parent_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000235822A30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000235822A30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'_children_with_property_name': "
     # "Field(name='_children_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000235822A30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000235822A30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x0000023584D6E040>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x0000023584D35F70>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x0000023584D6E160>, '__hash__': None})), ('__dir__', <method '__dir__' of "
     # "'object' objects>), ('__doc__', 'ChildrenWithProperty(parent_name: str, "
     # "_children_with_property_name: str)'), ('__eq__', <function "
     # "__create_fn__.<locals>.__eq__ at 0x0000023584D6E160>), ('__format__', "
     # "<method '__format__' of 'object' objects>), ('__ge__', <slot wrapper "
     # "'__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', None), ('__init__', <function "
     # '__create_fn__.<locals>.__init__ at 0x0000023584D6E040>), '
     # "('__init_subclass__', <built-in method __init_subclass__ of type object at "
     # "0x0000023582E353B0>), ('__le__', <slot wrapper '__le__' of 'object' "
     # "objects>), ('__lt__', <slot wrapper '__lt__' of 'object' objects>), "
     # "('__module__', 'common.schema_classes_test'), ('__ne__', <slot wrapper "
     # "'__ne__' of 'object' objects>), ('__new__', <built-in method __new__ of type "
     # "object at 0x00007FFFA22B4E00>), ('__reduce__', <method '__reduce__' of "
     # "'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' "
     # "objects>), ('__repr__', <function __create_fn__.<locals>.__repr__ at "
     # "0x0000023584D35F70>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x0000023582E353B0>), ('__weakref__', <attribute '__weakref__' of 'Parent' "
     # "objects>), ('children_with_property_name', <property object at "
     # '0x0000023584D48EF0>)]')
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {'parent_name': <class 'str'>, '_children_with_property_name': <class 'str'>, 'return': None}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_dataclass_property3():
    obj = ChildrenAndParentWithProperty(_parent_with_property_name="parent_name", _children_with_property_name="child name")
    print()
    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'_parent_with_property_name': 'parent_name', '_children_with_property_name': 'child name'}

    # print(f"obj.__annotations__: {obj.__annotations__}")  # obj.__annotations__: {'_children_with_property_name': <class 'str'>}

     #    ("obj.__dir__(): ['_parent_with_property_name', "
     # "'_children_with_property_name', '__module__', '__annotations__', "
     # "'children_with_property_name', '__doc__', '__dataclass_params__', "
     # "'__dataclass_fields__', '__init__', '__repr__', '__eq__', '__hash__', "
     # "'parent_with_property_name', '__dict__', '__weakref__', '__str__', "
     # "'__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', "
     # "'__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', "
     # "'__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', "
     # "'__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # ("vars(obj): {'_parent_with_property_name': 'parent_name', ""'_children_with_property_name': 'child name'}")

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      '__annotations__': {'_children_with_property_name': <class 'str'>},
    # 'children_with_property_name': <property object at 0x000001994665FDB0>,
    # '__doc__': 'ChildrenAndParentWithProperty(_parent_with_property_name: str, _children_with_property_name: str)',
    # '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False),
    # '__dataclass_fields__': {'_parent_with_property_name': ...
    #                         '_children_with_property_name': ...
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # print(f"type(obj).__annotations__: {type(obj).__annotations__}")  # type(obj).__annotations__: {'_children_with_property_name': <class 'str'>}


     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__annotations__': "
     # "{'_children_with_property_name': <class 'str'>}, "
     # "'children_with_property_name': <property object at 0x000002AF7EEA8770>, "
     # "'__doc__': 'ChildrenAndParentWithProperty(_parent_with_property_name: str, "
     # "_children_with_property_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'_parent_with_property_name': "
     # "Field(name='_parent_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x000002AF7C3F30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x000002AF7C3F30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'_children_with_property_name': "
     # "Field(name='_children_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x000002AF7C3F30D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x000002AF7C3F30D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x000002AF7EEAF940>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x000002AF7EEAF8B0>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x000002AF7EEAFAF0>, '__hash__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

    # print(f"obj.parent_with_property_name: {obj.parent_with_property_name}")
    # print(f"obj.children_with_property_name: {obj.children_with_property_name}")


     #    ("inspect.getmembers(type(obj)): [('__annotations__', "
     # "{'_children_with_property_name': <class 'str'>}), ('__class__', <class "
     # "'type'>), ('__dataclass_fields__', {'_parent_with_property_name': "
     # "Field(name='_parent_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000241A28340D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000241A28340D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'_children_with_property_name': "
     # "Field(name='_children_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000241A28340D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000241A28340D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}), '
     # "('__dataclass_params__', "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)), '
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__annotations__': {'_children_with_property_name': <class 'str'>}, "
     # "'children_with_property_name': <property object at 0x00000241A530E220>, "
     # "'__doc__': 'ChildrenAndParentWithProperty(_parent_with_property_name: str, "
     # "_children_with_property_name: str)', '__dataclass_params__': "
     # '_DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '
     # "'__dataclass_fields__': {'_parent_with_property_name': "
     # "Field(name='_parent_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000241A28340D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000241A28340D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), '
     # "'_children_with_property_name': "
     # "Field(name='_children_with_property_name',type=<class "
     # "'str'>,default=<dataclasses._MISSING_TYPE object at "
     # '0x00000241A28340D0>,default_factory=<dataclasses._MISSING_TYPE object at '
     # '0x00000241A28340D0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '
     # "'__init__': <function __create_fn__.<locals>.__init__ at "
     # "0x00000241A531E310>, '__repr__': <function __create_fn__.<locals>.__repr__ "
     # "at 0x00000241A531E280>, '__eq__': <function __create_fn__.<locals>.__eq__ at "
     # "0x00000241A531E4C0>, '__hash__': None})), ('__dir__', <method '__dir__' of "
     # "'object' objects>), ('__doc__', "
     # "'ChildrenAndParentWithProperty(_parent_with_property_name: str, "
     # "_children_with_property_name: str)'), ('__eq__', <function "
     # "__create_fn__.<locals>.__eq__ at 0x00000241A531E4C0>), ('__format__', "
     # "<method '__format__' of 'object' objects>), ('__ge__', <slot wrapper "
     # "'__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', None), ('__init__', <function "
     # '__create_fn__.<locals>.__init__ at 0x00000241A531E310>), '
     # "('__init_subclass__', <built-in method __init_subclass__ of type object at "
     # "0x00000241A3208F40>), ('__le__', <slot wrapper '__le__' of 'object' "
     # "objects>), ('__lt__', <slot wrapper '__lt__' of 'object' objects>), "
     # "('__module__', 'common.schema_classes_test'), ('__ne__', <slot wrapper "
     # "'__ne__' of 'object' objects>), ('__new__', <built-in method __new__ of type "
     # "object at 0x00007FFFA22B4E00>), ('__reduce__', <method '__reduce__' of "
     # "'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' "
     # "objects>), ('__repr__', <function __create_fn__.<locals>.__repr__ at "
     # "0x00000241A531E280>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x00000241A3208F40>), ('__weakref__', <attribute '__weakref__' of "
     # "'ParentWithProperty' objects>), ('children_with_property_name', <property "
     # "object at 0x00000241A530E220>), ('parent_with_property_name', <property "
     # 'object at 0x00000241A52F1E00>)]')
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {'_parent_with_property_name': <class 'str'>, '_children_with_property_name': <class 'str'>, 'return': None}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_classic_class():
    expect_result = {'parent_name': "parent_name"}
    obj = ClassicParent(parent_name="parent_name")
    print()

    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': 'parent_name'}

     #    ("obj.__dir__(): ['parent_name', '__module__', '__init__', '__dict__', "
     # "'__weakref__', '__doc__', '__repr__', '__hash__', '__str__', "
     # "'__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', "
     # "'__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', "
     # "'__reduce__', '__subclasshook__', '__init_subclass__', '__format__', "
     # "'__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'parent_name': 'parent_name'}"

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      '__init__': <function ClassicParent.__init__ at 0x0000025BFCA489D0>,
    # '__dict__': <attribute '__dict__' of 'ClassicParent' objects>, '__weakref__': <attribute '__weakref__' of 'ClassicParent' objects>,
    # '__doc__': None}
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__init__': <function "
     # "ClassicParent.__init__ at 0x0000019099E989D0>, '__dict__': <attribute "
     # "'__dict__' of 'ClassicParent' objects>, '__weakref__': <attribute "
     # "'__weakref__' of 'ClassicParent' objects>, '__doc__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

     #    ("inspect.getmembers(type(obj)): [('__class__', <class 'type'>), "
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__init__': <function ClassicParent.__init__ at 0x00000295C5567430>, "
     # "'__dict__': <attribute '__dict__' of 'ClassicParent' objects>, "
     # "'__weakref__': <attribute '__weakref__' of 'ClassicParent' objects>, "
     # "'__doc__': None})), ('__dir__', <method '__dir__' of 'object' objects>), "
     # "('__doc__', None), ('__eq__', <slot wrapper '__eq__' of 'object' objects>), "
     # "('__format__', <method '__format__' of 'object' objects>), ('__ge__', <slot "
     # "wrapper '__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', <slot wrapper '__hash__' of 'object' "
     # "objects>), ('__init__', <function ClassicParent.__init__ at "
     # "0x00000295C5567430>), ('__init_subclass__', <built-in method "
     # "__init_subclass__ of type object at 0x00000295C3505A60>), ('__le__', <slot "
     # "wrapper '__le__' of 'object' objects>), ('__lt__', <slot wrapper '__lt__' of "
     # "'object' objects>), ('__module__', 'common.schema_classes_test'), ('__ne__', "
     # "<slot wrapper '__ne__' of 'object' objects>), ('__new__', <built-in method "
     # "__new__ of type object at 0x00007FFFA22B4E00>), ('__reduce__', <method "
     # "'__reduce__' of 'object' objects>), ('__reduce_ex__', <method "
     # "'__reduce_ex__' of 'object' objects>), ('__repr__', <slot wrapper '__repr__' "
     # "of 'object' objects>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x00000295C3505A60>), ('__weakref__', <attribute '__weakref__' of "
     # "'ClassicParent' objects>)]")
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_classic_class_inherit():
    expect_result = {'parent_name': "parent_name"}
    obj = ClassicChildren(parent_name="parent_name", children_name="children_name")
    print()

    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': 'parent_name', 'children_name': 'children_name'}

     #    ("obj.__dir__(): ['parent_name', 'children_name', '__module__', '__init__', "
     # "'__doc__', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', "
     # "'__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', "
     # "'__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', "
     # "'__reduce__', '__subclasshook__', '__init_subclass__', '__format__', "
     # "'__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'parent_name': 'parent_name', 'children_name': 'children_name'}"

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      '__init__': <function ClassicChildren.__init__ at 0x000002A82DE00AF0>,
    # '__doc__': None}
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__init__': <function "
     # "ClassicChildren.__init__ at 0x000001E130FD0AF0>, '__doc__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")
    # assert obj.__dict__ == expect_result

     #    ("inspect.getmembers(type(obj)): [('__class__', <class 'type'>), "
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__init__': <function ClassicChildren.__init__ at 0x0000015E431595E0>, "
     # "'__doc__': None})), ('__dir__', <method '__dir__' of 'object' objects>), "
     # "('__doc__', None), ('__eq__', <slot wrapper '__eq__' of 'object' objects>), "
     # "('__format__', <method '__format__' of 'object' objects>), ('__ge__', <slot "
     # "wrapper '__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', <slot wrapper '__hash__' of 'object' "
     # "objects>), ('__init__', <function ClassicChildren.__init__ at "
     # "0x0000015E431595E0>), ('__init_subclass__', <built-in method "
     # "__init_subclass__ of type object at 0x0000015E410E75D0>), ('__le__', <slot "
     # "wrapper '__le__' of 'object' objects>), ('__lt__', <slot wrapper '__lt__' of "
     # "'object' objects>), ('__module__', 'common.schema_classes_test'), ('__ne__', "
     # "<slot wrapper '__ne__' of 'object' objects>), ('__new__', <built-in method "
     # "__new__ of type object at 0x00007FFAAA3C4E00>), ('__reduce__', <method "
     # "'__reduce__' of 'object' objects>), ('__reduce_ex__', <method "
     # "'__reduce_ex__' of 'object' objects>), ('__repr__', <slot wrapper '__repr__' "
     # "of 'object' objects>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x0000015E410E75D0>), ('__weakref__', <attribute '__weakref__' of "
     # "'ClassicParent' objects>)]")
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")

def test_classic_class_class_var():
    expect_result = {'parent_name': "parent_name"}
    obj = ClassicChildrenWithClassVar(parent_name="parent_name")
    print()

    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': 'parent_name'}

     #    ("obj.__dir__(): ['parent_name', '__module__', 'class_var_children_name', "
     # "'__init__', '__doc__', '__dict__', '__weakref__', '__repr__', '__hash__', "
     # "'__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', "
     # "'__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', "
     # "'__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', "
     # "'__format__', '__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'parent_name': 'parent_name'}"

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      'class_var_children_name': 'class_var_children_name',
    #                      '__init__': <function ClassicChildrenWithClassVar.__init__ at 0x00000274F88BBB80>,
    # '__doc__': None}
    # print(f"type(obj).__dict__: {type(obj).__dict__}")


    # ("vars(type(obj)): {'__module__': 'common.schema_class', "
    #  "'class_var_children_name': 'class_var_children_name', '__init__': <function "
    #  "ClassicChildrenWithClassVar.__init__ at 0x00000274F88BBB80>, '__doc__': "
    #  'None}')
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

    # "inspect.getmembers(type(obj)): [('__class__', <class 'type'>), "
    #  "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
    #  "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
    #  "'class_var_children_name': 'class_var_children_name', '__init__': <function "
    #  "ClassicChildrenWithClassVar.__init__ at 0x0000029B64AB0670>, '__doc__': "
    #  "None})), ('__dir__', <method '__dir__' of 'object' objects>), ('__doc__', "
    #  "None), ('__eq__', <slot wrapper '__eq__' of 'object' objects>), "
    #  "('__format__', <method '__format__' of 'object' objects>), ('__ge__', <slot "
    #  "wrapper '__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
    #  "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
    #  "of 'object' objects>), ('__hash__', <slot wrapper '__hash__' of 'object' "
    #  "objects>), ('__init__', <function ClassicChildrenWithClassVar.__init__ at "
    #  "0x0000029B64AB0670>), ('__init_subclass__', <built-in method "
    #  "__init_subclass__ of type object at 0x0000029B62A2AAB0>), ('__le__', <slot "
    #  "wrapper '__le__' of 'object' objects>), ('__lt__', <slot wrapper '__lt__' of "
    #  "'object' objects>), ('__module__', 'common.schema_classes_test'), ('__ne__', "
    #  "<slot wrapper '__ne__' of 'object' objects>), ('__new__', <built-in method "
    #  "__new__ of type object at 0x00007FFAAA3C4E00>), ('__reduce__', <method "
    #  "'__reduce__' of 'object' objects>), ('__reduce_ex__', <method "
    #  "'__reduce_ex__' of 'object' objects>), ('__repr__', <slot wrapper '__repr__' "
    #  "of 'object' objects>), ('__setattr__', <slot wrapper '__setattr__' of "
    #  "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
    #  "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
    #  "('__subclasshook__', <built-in method __subclasshook__ of type object at "
    #  "0x0000029B62A2AAB0>), ('__weakref__', <attribute '__weakref__' of "
    #  "'ClassicParent' objects>), ('class_var_children_name', "
    #  "'class_var_children_name')]")
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_classic_class_property():
    obj = ClassicParentWithProperty(parent_name="parent_name")
    print()

    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'_parent_with_property_name': 'parent_name'}

    # ("obj.__dir__(): ['_parent_with_property_name', '__module__', '__init__', "
    #  "'parent_with_property_name', '__dict__', '__weakref__', '__doc__', "
    #  "'__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', "
    #  "'__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', "
    #  "'__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', "
    #  "'__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # "vars(obj): {'_parent_with_property_name': 'parent_name'}"

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      '__init__': <function ClassicParentWithProperty.__init__ at 0x000001B20BAEDC10>,
    # 'parent_with_property_name': <property object at 0x000001B20BADFC70>,
    # '__dict__': <attribute '__dict__' of 'ClassicParentWithProperty' objects>, '__weakref__': <attribute
    # '__weakref__' of 'ClassicParentWithProperty' objects>, '__doc__': None}
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # ("vars(type(obj)): {'__module__': 'common.schema_class', '__init__': <function "
    #  'ClassicParentWithProperty.__init__ at 0x000001B99761DC10>, '
    #  "'parent_with_property_name': <property object at 0x000001B99761BDB0>, "
    #  "'__dict__': <attribute '__dict__' of 'ClassicParentWithProperty' objects>, "
    #  "'__weakref__': <attribute '__weakref__' of 'ClassicParentWithProperty' "
    #  "objects>, '__doc__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

     #    "inspect.getmembers(type(obj)): [('__class__', <class 'type'>), "
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__init__': <function ClassicParentWithProperty.__init__ at "
     # "0x000001899AC48700>, 'parent_with_property_name': <property object at "
     # "0x000001899AC2EC20>, '__dict__': <attribute '__dict__' of "
     # "'ClassicParentWithProperty' objects>, '__weakref__': <attribute "
     # "'__weakref__' of 'ClassicParentWithProperty' objects>, '__doc__': None})), "
     # "('__dir__', <method '__dir__' of 'object' objects>), ('__doc__', None), "
     # "('__eq__', <slot wrapper '__eq__' of 'object' objects>), ('__format__', "
     # "<method '__format__' of 'object' objects>), ('__ge__', <slot wrapper "
     # "'__ge__' of 'object' objects>), ('__getattribute__', <slot wrapper "
     # "'__getattribute__' of 'object' objects>), ('__gt__', <slot wrapper '__gt__' "
     # "of 'object' objects>), ('__hash__', <slot wrapper '__hash__' of 'object' "
     # "objects>), ('__init__', <function ClassicParentWithProperty.__init__ at "
     # "0x000001899AC48700>), ('__init_subclass__', <built-in method "
     # "__init_subclass__ of type object at 0x0000018998C47910>), ('__le__', <slot "
     # "wrapper '__le__' of 'object' objects>), ('__lt__', <slot wrapper '__lt__' of "
     # "'object' objects>), ('__module__', 'common.schema_classes_test'), ('__ne__', "
     # "<slot wrapper '__ne__' of 'object' objects>), ('__new__', <built-in method "
     # "__new__ of type object at 0x00007FFAAA3C4E00>), ('__reduce__', <method "
     # "'__reduce__' of 'object' objects>), ('__reduce_ex__', <method "
     # "'__reduce_ex__' of 'object' objects>), ('__repr__', <slot wrapper '__repr__' "
     # "of 'object' objects>), ('__setattr__', <slot wrapper '__setattr__' of "
     # "'object' objects>), ('__sizeof__', <method '__sizeof__' of 'object' "
     # "objects>), ('__str__', <slot wrapper '__str__' of 'object' objects>), "
     # "('__subclasshook__', <built-in method __subclasshook__ of type object at "
     # "0x0000018998C47910>), ('__weakref__', <attribute '__weakref__' of "
     # "'ClassicParentWithProperty' objects>), ('parent_with_property_name', "
     # '<property object at 0x000001899AC2EC20>)]')
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_classic_class_property2():
    obj = ClassicChildrenWithProperty(parent_name="parent_name", children_name="child name")
    print()

    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'parent_name': 'parent_name', '_children_with_property_name': 'child name'}

    # ("obj.__dir__(): ['parent_name', '_children_with_property_name', '__module__', "
    #  "'__init__', 'children_with_property_name', '__doc__', '__dict__', "
    #  "'__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__', "
    #  "'__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', "
    #  "'__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', "
    #  "'__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', "
    #  "'__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # ("vars(obj): {'parent_name': 'parent_name', '_children_with_property_name': " "'child name'}")
    # pprint(f"vars(obj): {vars(obj)}")

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      '__init__': <function ClassicChildrenWithProperty.__init__ at 0x0000022A48C4DDC0>,
    # 'children_with_property_name': <property object at 0x0000022A48C3FDB0>,
    # '__doc__': None}
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

    # ("vars(type(obj)): {'__module__': 'common.schema_class', '__init__': <function "
    #  'ClassicChildrenWithProperty.__init__ at 0x000001E1B17A0DC0>, '
    #  "'children_with_property_name': <property object at 0x000001E1B17A9F40>, "
    #  "'__doc__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

     #    ("inspect.getmembers(type(obj)): [('__class__', <class 'type'>), "
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__init__': <function ClassicChildrenWithProperty.__init__ at "
     # "0x000001B85AF288B0>, 'children_with_property_name': <property object at "
     # "0x000001B85AF187C0>, '__doc__': None})), ('__dir__', <method '__dir__' of "
     # "'object' objects>), ('__doc__', None), ('__eq__', <slot wrapper '__eq__' of "
     # "'object' objects>), ('__format__', <method '__format__' of 'object' "
     # "objects>), ('__ge__', <slot wrapper '__ge__' of 'object' objects>), "
     # "('__getattribute__', <slot wrapper '__getattribute__' of 'object' objects>), "
     # "('__gt__', <slot wrapper '__gt__' of 'object' objects>), ('__hash__', <slot "
     # "wrapper '__hash__' of 'object' objects>), ('__init__', <function "
     # 'ClassicChildrenWithProperty.__init__ at 0x000001B85AF288B0>), '
     # "('__init_subclass__', <built-in method __init_subclass__ of type object at "
     # "0x000001B858E4B0D0>), ('__le__', <slot wrapper '__le__' of 'object' "
     # "objects>), ('__lt__', <slot wrapper '__lt__' of 'object' objects>), "
     # "('__module__', 'common.schema_classes_test'), ('__ne__', <slot wrapper "
     # "'__ne__' of 'object' objects>), ('__new__', <built-in method __new__ of type "
     # "object at 0x00007FFAAA3C4E00>), ('__reduce__', <method '__reduce__' of "
     # "'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' "
     # "objects>), ('__repr__', <slot wrapper '__repr__' of 'object' objects>), "
     # "('__setattr__', <slot wrapper '__setattr__' of 'object' objects>), "
     # "('__sizeof__', <method '__sizeof__' of 'object' objects>), ('__str__', <slot "
     # "wrapper '__str__' of 'object' objects>), ('__subclasshook__', <built-in "
     # 'method __subclasshook__ of type object at 0x000001B858E4B0D0>), '
     # "('__weakref__', <attribute '__weakref__' of 'ClassicParent' objects>), "
     # "('children_with_property_name', <property object at 0x000001B85AF187C0>)]")
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}")

    # type(obj).__init__().__annotations__: {}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_classic_class_property3():
    obj = ClassicChildrenAndParentWithProperty(parent_name="parent_name", children_name="child name")
    print()

    # print(f"obj.__dict__: {obj.__dict__}")  # obj.__dict__: {'_parent_with_property_name': 'parent_name', '_children_with_property_name': 'child name'}

    # ("obj.__dir__(): ['_parent_with_property_name', "
    #  "'_children_with_property_name', '__module__', '__init__', "
    #  "'children_with_property_name', '__doc__', 'parent_with_property_name', "
    #  "'__dict__', '__weakref__', '__repr__', '__hash__', '__str__', "
    #  "'__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', "
    #  "'__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', "
    #  "'__reduce__', '__subclasshook__', '__init_subclass__', '__format__', "
    #  "'__sizeof__', '__dir__', '__class__']")
    # pprint(f"obj.__dir__(): {obj.__dir__()}")

    # pprint(f"vars(obj): {vars(obj)}")  # ("vars(obj): {'_parent_with_property_name': 'parent_name', " "'_children_with_property_name': 'child name'}")

    # type(obj).__dict__: {'__module__': 'common.schema_class',
    #                      '__init__': <function ClassicChildrenAndParentWithProperty.__init__ at 0x000002B045EA30D0>,
    # 'children_with_property_name': <property object at 0x000002B045EA1310>,
    # '__doc__': None}
    # print(f"type(obj).__dict__: {type(obj).__dict__}")

     #    ("vars(type(obj)): {'__module__': 'common.schema_class', '__init__': <function "
     # 'ClassicChildrenAndParentWithProperty.__init__ at 0x000001FE485040D0>, '
     # "'children_with_property_name': <property object at 0x000001FE48500220>, "
     # "'__doc__': None}")
    # pprint(f"vars(type(obj)): {vars(type(obj))}")

     #    "inspect.getmembers(type(obj)): [('__class__', <class 'type'>), "
     # "('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), "
     # "('__dict__', mappingproxy({'__module__': 'common.schema_classes_test', "
     # "'__init__': <function ClassicChildrenAndParentWithProperty.__init__ at "
     # "0x000001B5E2951A60>, 'children_with_property_name': <property object at "
     # "0x000001B5E2952810>, '__doc__': None})), ('__dir__', <method '__dir__' of "
     # "'object' objects>), ('__doc__', None), ('__eq__', <slot wrapper '__eq__' of "
     # "'object' objects>), ('__format__', <method '__format__' of 'object' "
     # "objects>), ('__ge__', <slot wrapper '__ge__' of 'object' objects>), "
     # "('__getattribute__', <slot wrapper '__getattribute__' of 'object' objects>), "
     # "('__gt__', <slot wrapper '__gt__' of 'object' objects>), ('__hash__', <slot "
     # "wrapper '__hash__' of 'object' objects>), ('__init__', <function "
     # 'ClassicChildrenAndParentWithProperty.__init__ at 0x000001B5E2951A60>), '
     # "('__init_subclass__', <built-in method __init_subclass__ of type object at "
     # "0x000001B5E08FCDC0>), ('__le__', <slot wrapper '__le__' of 'object' "
     # "objects>), ('__lt__', <slot wrapper '__lt__' of 'object' objects>), "
     # "('__module__', 'common.schema_classes_test'), ('__ne__', <slot wrapper "
     # "'__ne__' of 'object' objects>), ('__new__', <built-in method __new__ of type "
     # "object at 0x00007FFAAA3C4E00>), ('__reduce__', <method '__reduce__' of "
     # "'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' "
     # "objects>), ('__repr__', <slot wrapper '__repr__' of 'object' objects>), "
     # "('__setattr__', <slot wrapper '__setattr__' of 'object' objects>), "
     # "('__sizeof__', <method '__sizeof__' of 'object' objects>), ('__str__', <slot "
     # "wrapper '__str__' of 'object' objects>), ('__subclasshook__', <built-in "
     # 'method __subclasshook__ of type object at 0x000001B5E08FCDC0>), '
     # "('__weakref__', <attribute '__weakref__' of 'ClassicParentWithProperty' "
     # "objects>), ('children_with_property_name', <property object at "
     # "0x000001B5E2952810>), ('parent_with_property_name', <property object at "
     # '0x000001B5E2952E50>)]')
    # pprint(f"inspect.getmembers(type(obj)): {inspect.getmembers(type(obj))}"

    # type(obj).__init__().__annotations__: {}
    print(f"type(obj).__init__().__annotations__: {type(obj).__init__.__annotations__}")


def test_get_attributes():
    lv4 = Level4(_lv1_instance_att_1="lv1_ins_att_1",
                 _lv2_instance_att_1="lv2_ins_att_1",
                 _lv3_instance_att_1="lv3_ins_att_1",
                 _lv4_instance_att_1="lv4_ins_att_1")

    def lv4_method(self):
        return
    lv4.lv4_method = lv4_method

    lv4.lv4_instance_att_2 = ["lv4_instance_att_2"]

    dynamic_setattr_attributes = {f"dynamic_setattr_attribute_{i}": i for i in range(10)}
    for attr_name, attr_val in dynamic_setattr_attributes.items():
        setattr(lv4, attr_name, attr_val)

    lv4_custom_members = [item for item in lv4.__dir__() if not item.startswith("_")]
    # lv4_methods = [member for member in lv4_custom_members if hasattr(lv4.__getattribute__(member), "__call__")]
    lv4_methods = [member for member in lv4_custom_members if hasattr(lv4.__getattribute__(member), "__call__")]
    lv4_attributes = [member for member in lv4_custom_members if member not in lv4_methods]
    print()
    print(f"lv4_methods: {lv4_methods}")
    print(f"lv4_attributes: {lv4_attributes}")

    class_attributes = set()
    for cls in Level4.__mro__:
        print()
        print(f"cls.__dict__: {cls.__dict__}")
        print(f"vars(cls): {vars(cls)}")

    assert set(lv4_methods) == {"lv1_method", "lv3_method", "lv4_method"}
    lv4_attribute_values = {attribute: lv4.__getattribute__(attribute) for attribute in lv4_attributes}
    expected_attributes = {
        "lv1_instance_att_1": "@property lv1_ins_att_1",
        "lv1_class_att_1": "lv1_class_att_1",
        "lv2_instance_att_1": "@property lv2_ins_att_1",
        "lv2_class_att_1": "lv2_class_att_1",
        "lv3_instance_att_1": "@property lv3_ins_att_1",
        "lv3_class_att_1": "lv3_class_att_1",
        "lv4_instance_att_1": "@property lv4_ins_att_1",
        "lv4_class_att_1": "lv4_class_att_1",
        "lv4_instance_att_2": ["lv4_instance_att_2"],
    }
    expected_attributes.update(dynamic_setattr_attributes)
    assert lv4_attribute_values == expected_attributes
