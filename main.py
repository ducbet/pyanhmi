from common.schema_class import PublicApi, PydanticPublicApi, PublicApiEntry
from cpthon_code.cy_test import c_called_func
from pyanhmi.Helper import Helper
from pyanhmi.ObjectCreator import ObjectCreator

loop_total = 10000


def called_func3():
    return 2


def called_func2():
    for i in range(loop_total):
        called_func3()


def called_func():
    for i in range(loop_total):
        called_func2()
    return 1997


@Helper.timer
def p_call_func():
    print(called_func())


@Helper.timer
def c_call_func():
    print(c_called_func())


@Helper.timer
def create(public_apis):
    def _create():
        PublicApi(count=public_apis["count"],
                  entries=[PublicApiEntry(**entry) for entry in public_apis["entries"]])

    for i in range(loop_total):
        _create()
    return _create()


@Helper.timer
def create_dummy(public_apis):
    def _create():
        entries = []
        for entry in public_apis["entries"]:
            API = entry["API"]
            Description = entry["Description"]
            Auth = entry["Auth"]
            HTTPS = entry["HTTPS"]
            Cors = entry["Cors"]
            Link = entry["Link"]
            Category = entry["Category"]
            entries.append(PublicApiEntry(API=API,
                                          Description=Description,
                                          Auth=Auth,
                                          HTTPS=HTTPS,
                                          Cors=Cors,
                                          Link=Link,
                                          Category=Category))
        PublicApi(count=public_apis["count"],
                  entries=entries)

    for i in range(loop_total):
        _create()
    return _create()


@Helper.timer
def pyanhmi_create(public_apis):
    for i in range(loop_total):
        ObjectCreator.create_obj(public_apis, PublicApi)
    return ObjectCreator.create_obj(public_apis, PublicApi)


@Helper.timer
def pydantic_create(public_apis):
    for i in range(loop_total):
        PydanticPublicApi(**public_apis)
    return PydanticPublicApi(**public_apis)


if __name__ == '__main__':
    p_call_func()
    c_call_func()

    # Config.MODE = Mode.CASTING
    #
    # public_apis = Helper.load_json("files_storage/public_apis.json")
    # # ObjectCreator.create_obj(public_apis, PublicApi)
    #
    #
    # create(public_apis)
    # create_dummy(public_apis)
    #
    # Config.MODE = Mode.DUCK
    # pyanhmi_create(public_apis)
    # #
    #
    # Config.MODE = Mode.DUCK_TEST
    # pyanhmi_create(public_apis)
    #
    # Config.MODE = Mode.CASTING
    # pyanhmi_create(public_apis)
    # cProfile.run('pyanhmi_create(public_apis)')

    # Config.MODE = Mode.STRICT
    # pyanhmi_create(public_apis)
    #
    # pydantic_create(public_apis)



    # print(ObjectCreator.time_debug)
