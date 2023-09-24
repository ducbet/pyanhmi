from abc import ABC, abstractmethod


class Cookbook(ABC):
    @staticmethod
    @abstractmethod
    def has(item):
        pass

    @staticmethod
    @abstractmethod
    def get(item):
        pass

    @staticmethod
    @abstractmethod
    def add(item):
        pass
