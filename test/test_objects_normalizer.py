import random
import typing
from typing import get_type_hints, Optional, Tuple, Dict, List, Any, Set, Union

from common.schema_class import Product, ProductDescription, ProductOuter
from common.schema_classes_test import ClassicParent, AttributeTypesChild, Level4, AttributeTypesParent, \
    AttributeTypesComposite
from objects_normalizer import TypeCheckManager
from objects_normalizer.ObjectAttributes.AnyTypeAttribute import AnyTypeAttribute
from objects_normalizer.Config import Config
from objects_normalizer.ObjectAttributes.DictTypeAttribute import DictTypeAttribute
from objects_normalizer.ObjectAttributes.ListTypeAttribute import ListTypeAttribute
from objects_normalizer.ObjectAttributes.TupleTypeAttribute import TupleTypeAttribute
from objects_normalizer.ObjectCreator import ObjectCreator
from objects_normalizer.ObjectAttributes.UnionTypeAttribute import UnionTypeAttribute
from objects_normalizer.objects_normalizer import ObjectsNormalizer


def test_hash_Att():
    try:
        ObjectCreator.create_obj({}, AttributeTypesParent)
    except:
        pass
    try:
        ObjectCreator.create_obj({}, AttributeTypesChild)
    except:
        pass

    any_1 = AnyTypeAttribute(int)
    any_2 = AnyTypeAttribute(str)
    list_str = ListTypeAttribute(List[str])
    list_int = ListTypeAttribute(List[int])
    list_dict_1 = ListTypeAttribute(List[Dict[str, str]])
    list_dict_2 = ListTypeAttribute(List[Dict[str, str]])
    list_dict_3 = ListTypeAttribute(List[Dict[str, int]])
    dict_obj_1 = DictTypeAttribute(Dict[str, AttributeTypesParent])
    dict_obj_2 = DictTypeAttribute(Dict[str, AttributeTypesParent])
    dict_obj_3 = DictTypeAttribute(Dict[str, str])
    dict_obj_4 = DictTypeAttribute(Dict[str, AttributeTypesChild])

    uniton_1 = UnionTypeAttribute(typing.Union[typing.Tuple[str, str], typing.Tuple[int, int]])
    uniton_2 = UnionTypeAttribute(typing.Union[typing.Tuple[int, int], typing.Tuple[str, str]])

    uniton_obj_1 = UnionTypeAttribute(typing.Union[typing.Tuple[str, AttributeTypesParent], typing.Tuple[int, AttributeTypesChild]])
    uniton_obj_2 = UnionTypeAttribute(typing.Union[typing.Tuple[int, AttributeTypesChild], typing.Tuple[str, AttributeTypesParent]])

    assert len({any_1, any_2}) == 1
    assert len({list_str, list_int}) == 1
    assert len({list_dict_1, list_dict_2, list_dict_3}) == 1

    s = {dict_obj_1, dict_obj_2, dict_obj_3}
    assert len(s) == 2
    assert dict_obj_1 in s or dict_obj_2 in s
    assert dict_obj_3 in s

    s = {dict_obj_1, dict_obj_4}
    assert len(s) == 2

    assert len({uniton_1, uniton_2}) == 1  # union args order is not affected
    assert len({uniton_obj_1, uniton_obj_2}) == 1  # union args order is not affected

    # set_atts = {uniton_obj_1, uniton_obj_2}
    # print(f"set_atts: {len(set_atts)}, {set_atts}")


def test_sort_union_args():
    try:
        ObjectCreator.create_obj({}, AttributeTypesParent)
    except:
        pass
    value_atts = UnionTypeAttribute(Union[int, str, Any]).value_atts
    assert len(value_atts) == 1
    assert value_atts[0].__class__ == AnyTypeAttribute

    value_atts = UnionTypeAttribute(Union[int, List[str]]).value_atts
    assert len(value_atts) == 2
    assert value_atts[0].__class__ == ListTypeAttribute
    assert value_atts[1].__class__ == AnyTypeAttribute

    value_atts = UnionTypeAttribute(Union[int, List[str], List[int]]).value_atts
    assert len(value_atts) == 2
    assert value_atts[0].__class__ == ListTypeAttribute
    assert value_atts[1].__class__ == AnyTypeAttribute

    value_atts = UnionTypeAttribute(Union[List[str], int, Dict[str, int]]).value_atts
    assert len(value_atts) == 3
    assert value_atts[-1].__class__ == AnyTypeAttribute

    value_atts = UnionTypeAttribute(Union[List[str], int, Dict[str, AttributeTypesParent]]).value_atts
    assert len(value_atts) == 3
    assert value_atts[0].__class__ == DictTypeAttribute
    assert value_atts[1].__class__ == ListTypeAttribute


def test_get_att_priority():
    try:
        ObjectCreator.create_obj({}, AttributeTypesParent)
    except:
        pass
    try:
        ObjectCreator.create_obj({}, AttributeTypesChild)
    except:
        pass
    assert AnyTypeAttribute(str).get_att_priority() == Config.AnyAtt_priority
    assert ListTypeAttribute(typing.List[int]).get_att_priority() == Config.ListAtt_priority
    assert DictTypeAttribute(typing.Dict[str, AttributeTypesParent]).get_att_priority() == Config.ObjAtt_priority
    assert ListTypeAttribute(typing.List[AttributeTypesParent]).get_att_priority() == Config.ObjAtt_priority
    assert UnionTypeAttribute(typing.Union[typing.Dict[str, AttributeTypesParent], typing.Tuple[str, int]]).get_att_priority() == Config.ObjAtt_priority
    assert ListTypeAttribute(typing.List[str]).get_att_priority() == Config.ListAtt_priority
    assert UnionTypeAttribute(Optional[Tuple[Dict[str, Union[List[AttributeTypesParent], Set[int]]], Any]]).get_att_priority() == Config.ObjAtt_priority
    assert UnionTypeAttribute(Optional[Tuple[Dict[str, Union[List[str], Set[int]]], Any]]).get_att_priority() == Config.TupleAtt_priority


def test_create_obj():
    # todo: fix
    print("test_create_obj"),
    data = {
        "a_dict":{"a_dict_key": "a_dict_val"},
        "a_Optional": ({
                           "a_Optional_key_list": [
                               {
                                   "a_tuple": ("a_Optional_parent_1", "a_Optional_parent_2")
                               }
                           ],
                           "a_Optional_key_set": {1,5,8}
                       }, 5.2),
        "a_Any": Level4,
        "a_attParent": {"a_tuple": ("a_attParent_1", "a_attParent_2")},
        "a_DefaultDict": {
            "a_DefaultDict_key": [
                {"a_List": [{"a_tuple": ("a_DefaultDict_1", "a_DefaultDict_2")}]}
            ]
        }
    }
    # AttributeTypesChild(
    #
    #
    # )
    ObjectCreator.create_obj(data, AttributeTypesChild)
    return

    obj = ObjectCreator.create_obj({"parent_name": "pt_name"}, ClassicParent)
    assert obj.parent_name == "pt_name"

    obj = ObjectCreator.create_obj({"parent_name": "pt_name", "product_name": "Pro"}, ClassicParent)
    assert obj.parent_name == "pt_name"

    try:
        ObjectCreator.create_obj({}, ClassicParent)
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'parent_name'"

    try:
        ObjectCreator.create_obj({"product_name": "Pro"}, ClassicParent)
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'parent_name'"


def test_create_sources():
    data = {
        "id": 5,
        "product_id": 5,
        "description": "Pro 5 Desc",
        "image": "",
        "name": "Pro",
    }
    objects_normalizer = ObjectsNormalizer()
    product, product_description = objects_normalizer.create_sources(data, Product, ProductDescription)

    assert product.id == 5
    assert product.name == "Pro"

    assert product_description.product_id == 5
    assert product_description.description == "Pro 5 Desc"
    assert product_description.image == ""


def test_set_normalize_rule():
    # todo: fix
    # product = Product(id=1, name="Pro")
    # product_description = ProductDescription(product_id=5, description="Pro 5 Desc")

    objects_normalizer = ObjectsNormalizer()
    # objects_normalizer.add(product)
    #
    # product_rules = product.__getattribute__(ObjectsNormalizer.normalize_rules_field_name)
    #
    # assert product_rules["id"].localized_field_name == "id"
    # assert product_rules["id"].normalized_field_name == "product_id"
    # assert product_rules["id"].getter_func_name == "id"
    # assert product_rules["name"].localized_field_name == "name"
    # assert product_rules["name"].normalized_field_name == "product_name"
    # assert product_rules["name"].getter_func_name == "name"
    #
    # objects_normalizer.add(product_description)
    # product_description_rules = product_description.__getattribute__(ObjectsNormalizer.normalize_rules_field_name)
    # assert product_description_rules["description"].localized_field_name == "description"
    # assert product_description_rules["description"].normalized_field_name == "product_description"
    # assert product_description_rules["description"].getter_func_name == "normalize_description"
    # assert product_description_rules["product_id"].localized_field_name == "product_id"
    # assert product_description_rules["product_id"].normalized_field_name == "product_id"
    # assert product_description_rules["product_id"].getter_func_name == "product_id"
    # assert product_description_rules["image"].localized_field_name == "image"
    # assert product_description_rules["image"].normalized_field_name == "image"
    #
    # assert objects_normalizer.cached_classes == {type(product), type(product_description)}

    product = ProductOuter(id=1, name="Pro", details=[])
    objects_normalizer.add(product)
    product_rules = product.__getattribute__(Config.normalize_rules_field_name)
    print(f"product_rules: {product_rules}")

def test_add_source():
    product = Product(id=1, name="Pro")
    product_2 = Product(id=2, name="Pro 2")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")

    objects_normalizer = ObjectsNormalizer()
    objects_normalizer.add(product)

    assert (0, product) == objects_normalizer.sources[type(product)][0]

    objects_normalizer.add(product_2)
    assert (1, product_2) == objects_normalizer.sources[type(product_2)][1]

    objects_normalizer.add(product_description)
    assert (2, product_description) == objects_normalizer.sources[type(product_description)][0]

    objects_normalizer.add(product)
    assert (3, product) == objects_normalizer.sources[type(product)][2]

    source_count = 0
    for sources in objects_normalizer.sources.values():
        source_count += len(sources)
    assert source_count == objects_normalizer.obj_count


def test_export():
    # todo: fix
    product = Product(id=1, name="Pro")
    product_2 = Product(id=2, name="Pro 2")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")
    objects_normalizer = ObjectsNormalizer()

    objects_normalizer.add(product)
    assert objects_normalizer.export() == {
        "product_id": 1,
        "product_name": "Pro",
    }
    assert objects_normalizer.export(["product_id"]) == {
        "product_id": 1,
    }

    objects_normalizer.add(product_2)
    assert objects_normalizer.export() == {
        "product_id": 2,
        "product_name": "Pro 2",
    }

    objects_normalizer.add(product_description)
    assert objects_normalizer.export() == {
        "product_id": 5,
        "product_description": "normalized Pro 5 Desc",
        "product_name": "Pro 2",
        "image": "",
    }

    objects_normalizer.add(product)
    assert objects_normalizer.export(["product_id", "product_name"]) == {
        "product_id": 1,
        "product_name": "Pro",
    }
    assert objects_normalizer.export(["product_id", "product_description"]) == {
        "product_id": 1,
        "product_description": "normalized Pro 5 Desc",
    }
    assert objects_normalizer.export() == {
        "product_id": 1,
        "product_description": "normalized Pro 5 Desc",
        "product_name": "Pro",
        "image": "",
    }


def test_get_latest_objs():
    data = {
        "id": 5,
        "product_id": 5,
        "description": "Pro 5 Desc",
        "image": "",
        "name": "Pro",
    }
    objects_normalizer = ObjectsNormalizer(data, Product, ProductDescription)
    product = objects_normalizer.get_latest_objs(Product)
    assert product is ObjectsNormalizer.get_real_obj(objects_normalizer.sources[Product][-1])

    product, product_description = objects_normalizer.get_latest_objs(Product, ProductDescription)

    assert product is ObjectsNormalizer.get_real_obj(objects_normalizer.sources[Product][-1])
    assert product_description is ObjectsNormalizer.get_real_obj(objects_normalizer.sources[ProductDescription][-1])

    try:
        objects_normalizer.get_latest_objs(ClassicParent)
    except IndexError as e:
        assert "list index out of range" in str(e)
    try:
        objects_normalizer.get_latest_objs(None)
    except IndexError as e:
        assert "list index out of range" in str(e)
    try:
        objects_normalizer.get_latest_objs(Product, None)
    except IndexError as e:
        assert "list index out of range" in str(e)
    try:
        objects_normalizer.get_latest_objs(Product, ClassicParent)
    except IndexError as e:
        assert "list index out of range" in str(e)


def test_get_all_objs():
    product = Product(id=1, name="Pro")
    product_2 = Product(id=2, name="Pro 2")
    product_description = ProductDescription(product_id=5, description="Pro 5 Desc")
    objects_normalizer = ObjectsNormalizer()

    objects_normalizer.add(product)
    assert objects_normalizer.get_all_objs() == [product]

    objects_normalizer.add(product_description)
    assert objects_normalizer.get_all_objs() == [product, product_description]

    objects_normalizer.add(product_2)
    assert objects_normalizer.get_all_objs() == [product, product_description, product_2]

    objects_normalizer.add(product_description)
    assert objects_normalizer.get_all_objs() == [product, product_description, product_2, product_description]

    objs = [product, product_2, product_description]
    rand_total = 10
    rand_result = []
    for _ in range(rand_total):
        rand_obj = random.choice(objs)
        objects_normalizer.add(rand_obj)
        rand_result.append(rand_obj)

    assert objects_normalizer.get_all_objs() == [product, product_description, product_2, product_description] + rand_result


def test_get_normalizable_fields():
    normalizable_fields = TypeCheckManager.get_normalizable_fields(AttributeTypesChild)
    assert normalizable_fields == {AttributeTypesChild, AttributeTypesParent}
