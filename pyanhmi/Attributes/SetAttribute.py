import typing
from collections.abc import Iterable
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import Attribute
from common.Config import Config
from pyanhmi.Cookbook.CookbookAttributes import CookbookAttributes
from common.Error import InvalidDatatype


@CookbookAttributes.add
@dataclass
class SetAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [set]

    def __init__(self, field_type):
        super().__init__(field_type)
        args_type = typing.get_args(field_type)
        if not args_type:
            self.value_att = CookbookAttributes.get(None)
            return
        self.value_att = CookbookAttributes.get(args_type[0])

    def get_att_priority(self):
        return max(Config.SetAtt_priority, self.value_att.get_att_priority())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value_att})"

    def get_hash_content(self):
        return self.__class__, self.value_att.get_hash_content()

    def __hash__(self):
        return hash(self.get_hash_content())

    def strict_create(self, data):
        if not isinstance(data, set):
            raise InvalidDatatype(expects=set, data=data)
        return set(self.value_att.strict_create(v) for v in data)

    def casting_create(self, data: typing.Union[set, Iterable]):
        if isinstance(data, set) or isinstance(data, Iterable):
            return set(self.value_att.casting_create(v) for v in data)
        raise InvalidDatatype(expects=[set, Iterable], data=data)
