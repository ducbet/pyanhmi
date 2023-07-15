from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any

from common.Config import Mode


class Attribute(ABC):
    TYPES = []  # will be declared in children

    def __init__(self, field_type):
        self.field_type = field_type

    def __lt__(self, other):
        return self.get_att_priority() < other.get_att_priority()

    def __repr__(self):
        # print(f"ObjectAttribute: __repr__ ",  f"{self.__class__.__name__}({self.field_type})")
        return f"{self.__class__.__name__}({self.field_type})"

    def create(self, data: Any, mode: Mode):
        if mode is Mode.CASTING:
            return self.casting_create(data)
        if mode is Mode.STRICT:
            return self.strict_create(data)
        if mode is Mode.DUCK:
            return data
        if mode is Mode.DUCK_TEST:
            return self.duck_test_create(data)

    @abstractmethod
    def duck_test_create(self, data):
        # only for testing performance
        pass

    @abstractmethod
    def strict_create(self, data):
        pass

    @abstractmethod
    def casting_create(self, data):
        pass

    @staticmethod
    def is_iterable_but_not_str(data):
        return not isinstance(data, str) and isinstance(data, Iterable)
