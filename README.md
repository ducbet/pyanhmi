<b>Problem</b>: Complex systems often use multiple databases simultaneously (MySQL, Redis, Elasticsearch,...).<br>
So that, one value can be stored in various places with different keys.<br>
For example, the "UserName" field can be named as "username", "name", "user_name" or "UserName".<br>
This makes object initialization and conversion scripts become bulky.

<b>Target</b>: Create a library that simplifies the object initialization and data conversion process.

<b>Idea</b>: https://note.com/airitech/n/n14e7f1d908c1


<b>Usage</b>:
1. Define `PYANHMI_RECIPE` for each object type (instructions for creating objects). Either by defining it inside the class or providing it when creating the object.
2. Create objects (or use existing objects)
3. Add objects to `LunchBox` (manage the added objects)
4. Use `lunchbox.export()` to export data to a dictionary or `lunchbox.convert(TargetType)` to create an object of type `TargetType`
```
    # 1. Define instructions for each object type
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

    # 2. Create objects (or use existing objects)
    # Create object in the normal way
    user_1 = UserDb1(email='tmd@gmail.com', name='Trieu Duc', address='Ba Dinh, Ha Noi')
    
    db_2_users = {
        "user_email": "tmd@gmail.com",
        "full_name": "Trieu Minh Duc",
        "first_name": "Trieu",
        "last_name": "Duc",
    }

    # Automatically create object using pyanhmi
    user_2 = create(db_2_users, UserDb2)
    print(user_2)  # output: UserDb2(user_email='tmd@gmail.com', full_name='Trieu Minh Duc', first_name='Trieu', last_name='Duc')

    # 3. Add objects to lunchbox
    lunchbox = LunchBox()
    lunchbox.add(user_1)
    lunchbox.add(user_2)
    
    # 4. Use `lunchbox.export()` to export data to a dictionary
    assert lunchbox.export() == {'user_name': 'Trieu Minh Duc',
                                 'user_email': 'tmd@gmail.com',
                                 'first_name': 'Trieu',
                                 'last_name': 'Duc',
                                 'address': 'Ba Dinh, Ha Noi'}
    
    # 4. Use `lunchbox.convert(ReportUser)` to create an object of type `ReportUser`
    assert lunchbox.convert(ReportUser) == ReportUser(mail=user_2.user_email,
                                                      name=user_2.full_name,
                                                      first_name=user_2.first_name,
                                                      last_name=user_2.last_name,
                                                      address=user_1.address)
```

<b>Features</b>:
- Initialize objects recursively from a dictionary: Do not need to inherit from BaseModel like other libraries. You can use pyanhmi with minimal changes to existing classes
    ```
      @dataclass
      class NestedObj:
          nested: tuple
    
    
      @dataclass
      class OuterObj:
          outer: Optional[Tuple[Dict[str, Union[List[NestedObj], Set[int]]], typing.DefaultDict[str, int]]]


      Config.MODE = CastingMode.STRICT
      data = {
        "outer": (
            {
                "outer_list": [  # List[NestedObj]
                    {
                        "nested": ("nested_tuple_1", "nested_tuple_2"),  # nested_tuple: tuple
                    }
                ],
                "outer_set": {1, 5, 8}  # Set[int]
            },
            {"key": 2}  # typing.DefaultDict[str, int]
        )
    }
    outer_obj = create(data, OuterObj)
    print(outer_obj)
    # output: OuterObj(outer=({'outer_list': [NestedObj(nested=('nested_tuple_1', 'nested_tuple_2'))], 'outer_set': {8, 1, 5}}, defaultdict(<class 'int'>, {'key': 2})))

    assert isinstance(outer_obj.outer, tuple)

    assert isinstance(outer_obj.outer[0], dict)
    assert isinstance(outer_obj.outer[1], typing.DefaultDict)
    outer_obj.outer[1]["new_key"] += 19
    print(outer_obj.outer[1])  # output: defaultdict(<class 'int'>, {'key': 2, 'new_key': 19})
    ```
- Strict mode: Raise an error if the data does not match the type defined in the class.  
```
  Config.MODE = CastingMode.STRICT
  db_1_users = {
    "name": "Trieu Duc",
    "email": "tmd@gmail.com",
    "address": 10000,
  }
  try:
    create(db_1_users, UserDb1)
  except InvalidDatatype as e:
    assert e == InvalidDatatype(expects=str, data=10000)
```
- Casting mode: Automatically cast types as defined in the class
```
  Config.MODE = CastingMode.CASTING
  db_1_users = {
    "name": "Trieu Duc",
    "email": "tmd@gmail.com",
    "address": 10000,
  }
  user = create(db_1_users, UserDb1)
  assert user.address == "10000"
```
- Define functions that will be executed to standardize/change attribute values before/after object initialization (under development)
```
    product_description = ProductDescription(product_id=1, description="ipad Pro 5 Desc")
    lunchbox = LunchBox()
    lunchbox.add(product_description)
    print(lunchbox.export())
    # output: {'product_description': 'IPAD PRO 5 DESC', 'image': '', 'product_id': 1}
    # ※ upper description when exporting
```
- Export to dictionary or convert to another object. Priority order is `LIFO` and not override. Customize output with parameters: `export_order`, `is_override`
```
    @dataclass
    class Product:
        id: int
        name: str
    
        PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
            ingredients={
                "id": Field(alias="product_id"),
                "name": Field(alias="product_name"),
            }
        )
    
    @dataclass
    class Product2:
        id: int
        name: str = "sample name"
        description: str = "sample des"
    
        PYANHMI_RECIPE: ClassVar[Recipe] = Recipe(
            ingredients={
                "id": Field(alias="product_id"),
                "name": Field(alias="product_name"),
                "description": Field(alias="product_description"),
            }
        )
    
    Config.MODE = CastingMode.CASTING
    product = Product(id=1, name="Pro")
    product_1 = Product(id=1, name="ipad Pro")
    product_2 = Product2(id=1)
    
    lunchbox = LunchBox()
    lunchbox.add(product)
    lunchbox.add(product_1)
    lunchbox.add(product_2)
    assert lunchbox.export() == {
        "product_id": 1,
        "product_name": "ipad Pro",  # product_1
        "product_description": "sample des",  # product_2
    }
    assert lunchbox.export(export_order=ExportOrder.FIFO) == {
        "product_id": 1,
        "product_name": "Pro",  # product
        "product_description": "sample des",  # product_2
    }
    assert lunchbox.export(is_override=True) == {
        "product_id": 1,
        "product_name": "sample name",  # product_2
        "product_description": "sample des",  # product_2
    }
```

<b>More info</b>:
- Please check test files for more examples
  - https://github.com/ducbet/pyanhmi/blob/master/test/test_objects_normalizer.py
  - https://github.com/ducbet/pyanhmi/blob/master/test/test_readme.py
- Supported types when initializing object: https://github.com/ducbet/pyanhmi/tree/master/pyanhmi/Attributes