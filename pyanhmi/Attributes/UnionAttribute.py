import typing
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import Attribute
from common.Config import Config
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype


@CookbookAttributes.add
@dataclass
class UnionAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [typing.Union]

    def __init__(self, field_type):
        super().__init__(field_type)
        self.args = typing.get_args(field_type)
        self.value_atts = [CookbookAttributes.get(arg) for arg in self.args]

        # todo: smart onion
        # self.smart_union_value_atts = set()
        # self.smart_union_value_atts = sorted(self.value_atts, reverse=True)
        # if any_attribute:
        #     self.smart_union_value_atts.remove(any_attribute)
        #     self.smart_union_value_atts = list(self.smart_union_value_atts)
        #     self.smart_union_value_atts.append(any_attribute)
        # else:
        #     self.smart_union_value_atts = list(self.smart_union_value_atts)

    def get_att_priority(self):
        if not self.value_atts:
            return Config.UnionAtt_priority
        return max(Config.UnionAtt_priority, *[field.get_att_priority() for field in self.value_atts])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value_atts})"

    def get_hash_content(self):
        hash_content = [self.__class__]
        for field in self.value_atts:
            hash_content.append(field.get_hash_content())
        return tuple(hash_content)

    def __hash__(self):
        # print(f"UnionAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def _get_expect_types(self):
        result = []
        for arg in self.args:
            origin = typing.get_origin(arg)
            if origin:
                result.append(origin)
            else:
                result.append(arg)
        return result

    def strict_create(self, data):
        for value_att in self.value_atts:
            try:
                return value_att.strict_create(data)
            except InvalidDatatype:
                pass
        raise InvalidDatatype(expects=self._get_expect_types(), data=data)

    def casting_create(self, data):
        for value_att in self.value_atts:
            try:
                return value_att.casting_create(data)
            except InvalidDatatype:
                pass
        raise InvalidDatatype(expects=self._get_expect_types(), data=data)

    def duck_test_create(self, data):
        for value_att in self.value_atts:
            try:
                return value_att.duck_test_create(data)
            except InvalidDatatype:
                pass
