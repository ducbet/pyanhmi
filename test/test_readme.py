import typing

import pytest

from common.Config import Config, CastingMode, ExportOrder
from common.Error import InvalidDatatype
from common.demo_schema_class import UserDb1, UserDb2, ReportUser, OuterObj, NestedObj
from common.schema_class import ProductDescription, Product, Product2, ConvertedProduct
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create
from pyanhmi.LunchBox import LunchBox


@pytest.fixture
def mode_duck():
    CookbookRecipe.clear()
    Config.MODE = CastingMode.DUCK


@pytest.fixture
def mode_casting():
    CookbookRecipe.clear()
    Config.MODE = CastingMode.CASTING


@pytest.fixture
def mode_strict():
    CookbookRecipe.clear()
    Config.MODE = CastingMode.STRICT


def test_convert(mode_strict):
    user_1 = UserDb1(email='tmd@gmail.com', name='Trieu Duc', address='Ba Dinh, Ha Noi')

    db_2_users = {
        "user_email": "tmd@gmail.com",
        "full_name": "Trieu Minh Duc",
        "first_name": "Trieu",
        "last_name": "Duc",
    }
    user_2 = create(db_2_users, UserDb2)
    print(user_2)  # output: UserDb2(user_email='tmd@gmail.com', full_name='Trieu Minh Duc', first_name='Trieu', last_name='Duc')

    lunchbox = LunchBox()
    lunchbox.add(user_1)
    lunchbox.add(user_2)
    assert lunchbox.convert(ReportUser) == ReportUser(mail=user_2.user_email,
                                                      name=user_2.full_name,
                                                      first_name=user_2.first_name,
                                                      last_name=user_2.last_name,
                                                      address=user_1.address)
    assert lunchbox.export() == {'user_name': 'Trieu Minh Duc',
                                 'user_email': 'tmd@gmail.com',
                                 'first_name': 'Trieu',
                                 'last_name': 'Duc',
                                 'address': 'Ba Dinh, Ha Noi'}


def test_create_nested_object(mode_strict):
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

    assert isinstance(list((outer_obj.outer[0].values()))[0], list)
    assert isinstance(list((outer_obj.outer[0].values()))[1], set)

    assert isinstance(list((outer_obj.outer[0].values()))[0][0], NestedObj)
    assert isinstance(list(list((outer_obj.outer[0].values()))[1])[0], int)

    assert isinstance(list((outer_obj.outer[0].values()))[0][0].nested, tuple)


def test_casting_strict(mode_strict):
    db_1_users = {
        "name": "Trieu Duc",
        "email": "tmd@gmail.com",
        "address": 10000,
    }
    try:
        create(db_1_users, UserDb1)
    except InvalidDatatype as e:
        assert e == InvalidDatatype(expects=str, data=10000)


def test_casting(mode_casting):
    db_1_users = {
        "name": "Trieu Duc",
        "email": "tmd@gmail.com",
        "address": 10000,
    }
    user = create(db_1_users, UserDb1)
    assert user.address == "10000"


def test_export(mode_strict):
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


def test_action(mode_strict):
    product_description = ProductDescription(product_id=1, description="ipad Pro 5 Desc")
    lunchbox = LunchBox()
    lunchbox.add(product_description)
    print(lunchbox.export())