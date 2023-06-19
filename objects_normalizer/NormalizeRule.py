from objects_normalizer.TypeCheckManager import TypeCheckManager


class NormalizeRule:
    def __init__(self, localized_field_name: str, field_type, normalized_field_name: str = "", getter_func_name: str = ""):
        self.localized_field_name = localized_field_name
        self.normalized_field_name = normalized_field_name
        self.getter_func_name = getter_func_name
        self.is_ignored = False
        self.field_type = field_type
        self.is_final_att = TypeCheckManager.is_final_type(field_type)
        self.auto_init = None if self.is_final_att else self.get_auto_init(field_type)
        print(f"get_auto_init. field_type: {field_type}, self.auto_init: {self.auto_init}")
        # print()

    def create(self, data):
        # print(f"NormalizeRule: data {data}, self.auto_init: {self.auto_init}")
        return self.auto_init.create(data)

    def get_auto_init(self, field_type):
        # print(f"get_auto_init. field_type: {field_type}")
        # print(f"TypeCheckManager.get_TypeManager(field_type): {TypeCheckManager.get_TypeManager(field_type)}")
        return TypeCheckManager.get_TypeManager(field_type)(field_type)
        # pass

    def is_normalize(self):
        return False

    @property
    def normalized_field_name(self) -> str:
        if not self._normalized_field_name:
            return self.localized_field_name
        return self._normalized_field_name

    @normalized_field_name.setter
    def normalized_field_name(self, normalized_field_name):
        self._normalized_field_name = normalized_field_name

    @property
    def getter_func_name(self) -> str:
        # print(f"@property getter_func_name, self._getter_func_name: {self._getter_func_name}")
        if not self._getter_func_name:
            # print(f"@property if not self._getter_func_name")
            return self.localized_field_name
        return self._getter_func_name

    @getter_func_name.setter
    def getter_func_name(self, func_name):
        self._getter_func_name = func_name

    def __eq__(self, other: "NormalizeRule"):
        return (self.normalized_field_name == other.normalized_field_name and self.getter_func_name == other.getter_func_name)

    def __repr__(self):
        return f"NormalizeRule(" \
               f"localized_field_name: {self.localized_field_name}, " \
               f"field_type: {self.field_type}, " \
               f"auto_init: {self.auto_init}, " \
               f"is_normalize: {self.is_normalize()}, " \
               f"normalized_field_name: {self.normalized_field_name}, " \
               f"getter_func_name: {self.getter_func_name})"
