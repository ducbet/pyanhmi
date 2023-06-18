from common.schema_classes_test import Level4, AttributeTypesChild
from objects_normalizer.ObjectCreator import ObjectCreator

if __name__ == '__main__':
    # mysql_client = MysqlClient()
    # x = typing.Union[typing.Union[int, str], float]
    # y = typing.Union
    # z = typing.Optional[typing.Union[typing.Union[int, str], float]]
    # print(x, typing.get_origin(x), typing.get_args(x))
    # print(y, typing.get_origin(y))
    # print(z, typing.get_origin(z), typing.get_args(z))
    # exit()

    data = {
        "a_tuple": ("a_tuple_1", "a_tuple_2"),
        "a_dict": {"a_dict_key": "a_dict_val"},
        "a_Optional": ({
                           "a_Optional_key_list": [
                               {
                                   "a_tuple": ("a_Optional_parent_1", "a_Optional_parent_2")
                               }
                           ],
                           "a_Optional_key_set": {1, 5, 8}
                       }, 5.2),
        "a_Any": Level4,
        "a_attParent": {"a_tuple": ("a_attParent_1", "a_attParent_2")},
        "a_DefaultDict": {
            "a_DefaultDict_key": [
                {"a_List": [{"a_tuple": ("a_DefaultDict_1", "a_DefaultDict_2")}]}
            ]
        },
        "a_DefaultDict_int": {
            "a_DefaultDict_int_key": [1, 5, 7]
        }
    }
    tmp = ObjectCreator.create_obj(data, AttributeTypesChild)
    print()
    print(tmp)
    print()

