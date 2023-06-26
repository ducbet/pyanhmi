import inspect
import typing
from collections.abc import Mapping, Iterable
from dataclasses import dataclass

from pyanhmi.Attributes.Attribute import register_attribute, Attribute
from pyanhmi.Config import Config
from pyanhmi.Error import InvalidDatatype


@register_attribute
@dataclass
class DictAttribute(Attribute):
    TYPES: typing.ClassVar[list] = [dict]

    def __init__(self, field_type):
        super().__init__(field_type)
        args_type = typing.get_args(field_type)
        if not args_type:
            self.key_att = self.get_TypeManager(None)(None)
            self.value_att = self.get_TypeManager(None)(None)
            return
        self.key_type = args_type[0]
        self.key_att = self.get_TypeManager(self.key_type)(self.key_type)
        self.value_type = args_type[1]
        self.value_att = self.get_TypeManager(self.value_type)(self.value_type)

    def get_att_priority(self):
        return max(Config.DictAtt_priority, self.key_att.get_att_priority(), self.value_att.get_att_priority())

    def get_hash_content(self):
        return self.__class__, self.key_att.get_hash_content(), self.value_att.get_hash_content()

    def __hash__(self):
        # print(f"DictAtt: self.field_type: {self.field_type}, self.get_hash_content(): {self.get_hash_content()}")
        return hash(self.get_hash_content())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key_att}, {self.value_att})"

    def duck_create(self, data):
        try:
            return dict({self.key_att.duck_create(k): self.value_att.duck_create(v) for k, v in data.items()})
        except:
            return data

    def strict_create(self, data: dict):
        if not isinstance(data, dict):
            raise InvalidDatatype(expects=dict, data=data)
        return dict({self.key_att.strict_create(k): self.value_att.strict_create(v) for k, v in data.items()})

    def casting_create(self, data):
        if isinstance(data, dict):
            return {self.key_att.casting_create(k): self.value_att.casting_create(v) for k, v in data.items()}
        if isinstance(data, Iterable):
            if len(data) == 0:
                return dict()
            try:
                return dict({self.key_att.casting_create(v[0]): self.value_att.casting_create(v[1]) for v in data})
            except TypeError as e:
                raise InvalidDatatype(expects=Iterable, data=data)
            except IndexError:
                raise InvalidDatatype(expects=f"key-value {Iterable}", data=data)
        raise InvalidDatatype(expects=[dict, f"key-value {Iterable}"], data=data)
