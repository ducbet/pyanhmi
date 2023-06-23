import os
from dataclasses import dataclass


@dataclass
class NestedClass:
    id: int
    name: str

    @staticmethod
    def get_root_path():
        return os.path.abspath(__file__)