from collections import defaultdict
from typing import Tuple, Any

from pyanhmi.ObjectCreator import create
from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
from common.Config import Config
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe


class ObjectNormalizer:

    def __init__(self, data=None, *args):
        self.sources = defaultdict(list)
        self.obj_count = 0
        self.max_idx = 0
        for obj in self.create_sources(data, *args):
            self.add(obj)

    @property
    def is_obj_idx_continuous(self):
        return self.obj_count == self.max_idx

    @staticmethod
    def get_obj_idx(obj):
        return obj[0]

    @staticmethod
    def get_real_obj(obj):
        return obj[1]

    def add(self, obj):
        if not CookbookRecipe.has(type(obj)):
            CookbookRecipe.add(AuthenticRecipe(obj=obj))
        self.sources[type(obj)].append((self.obj_count, obj))
        self.obj_count += 1
        self.max_idx += 1

    def create_sources(self, data, *args):
        if not data or not args:
            return {}
        return tuple([create(data, obj_type) for obj_type in args])

    def get_latest_objs_of_each_source(self):
        """
        Get latest object in each source
        :return:
        """
        # select latest object in each source
        latest_objs = {cls: objs[-1] for cls, objs in self.sources.items()}
        return latest_objs

    def get_latest_objs(self, *args):
        """
        Return the latest obj in each source
        Raise IndexError if one of cls is not in source
        :return:
        """
        if len(args) == 0:
            return tuple([ObjectNormalizer.get_real_obj(self.sources[obj_type][-1]) for obj_type in self.sources.keys()])
        elif len(args) == 1:
            return ObjectNormalizer.get_real_obj(self.sources[args[0]][-1])
        else:
            return tuple([ObjectNormalizer.get_real_obj(self.sources[obj_type][-1]) for obj_type in args])

    @staticmethod
    def _get_obj_by_idx_in_slice(sources_slice: list, obj_idx: int) -> Tuple[int, Any]:
        for cls_idx in range(0, len(sources_slice)):
            if ObjectNormalizer.get_obj_idx(sources_slice[cls_idx]) == obj_idx:
                return cls_idx, sources_slice[cls_idx]
        return -1, None

    @staticmethod
    def _get_latest_obj_in_slice(sources_slice: list) -> Tuple[int, Any]:
        latest_obj = sources_slice[0]
        latest_idx = 0
        for idx in range(1, len(sources_slice)):
            if ObjectNormalizer.get_obj_idx(sources_slice[idx]) > ObjectNormalizer.get_obj_idx(latest_obj):
                latest_obj = sources_slice[idx]
                latest_idx = idx
        return latest_idx, latest_obj

    @staticmethod
    def _get_oldest_obj_in_slice(sources_slice: list) -> Tuple[int, Any]:
        """

        :param sources_slice:
        :return:
        """
        oldest_obj = sources_slice[0]
        oldest_idx = 0
        for cls_idx in range(1, len(sources_slice)):
            if ObjectNormalizer.get_obj_idx(sources_slice[cls_idx]) < ObjectNormalizer.get_obj_idx(oldest_obj):
                oldest_obj = sources_slice[cls_idx]
                oldest_idx = cls_idx
        return oldest_idx, oldest_obj

    def get_all_objs(self):
        """
        Get all objects of all sources by ascending order
        :return:
        """
        objs_idx = [0] * len(self.sources)
        sources_values = list(self.sources.values())

        result = []
        for obj_idx in range(self.obj_count):
            sources_slice = [sources_values[source_idx][source_obj_idx] if source_obj_idx != -1 else (self.max_idx, None)
                             for source_idx, source_obj_idx in enumerate(objs_idx)]
            oldest_idx, oldest_obj = self._get_obj_by_idx_in_slice(sources_slice, obj_idx) if self.is_obj_idx_continuous \
                else self._get_oldest_obj_in_slice(sources_slice)
            result.append(ObjectNormalizer.get_real_obj(oldest_obj))
            objs_idx[oldest_idx] += 1
            if objs_idx[oldest_idx] == len(sources_values[oldest_idx]):
                objs_idx[oldest_idx] = -1  # finish this source
        return result

    def export(self, target_normalize_fields=None):
        latest_sources = list(self.get_latest_objs_of_each_source().values())
        # sort by ascending order
        latest_sources.sort(key=lambda s: ObjectNormalizer.get_obj_idx(s))
        result = {}
        for i in range(len(latest_sources) - 1, -1, -1):
            if target_normalize_fields and set(target_normalize_fields) == set(result.keys()):
                # stop checking if all desired fields are collected
                 break
            source = ObjectNormalizer.get_real_obj(latest_sources[i])
            for field, rule in getattr(source, Config.PYANHMI_RECIPE).ingredients.items():
                if target_normalize_fields and rule.alias not in target_normalize_fields:
                    continue
                if rule.alias in result:
                    continue
                normalized_func = source.__getattribute__(rule.getter_func)
                if hasattr(normalized_func, "__call__"):
                    result[rule.alias] = normalized_func()  # call method
                else:
                    result[rule.alias] = normalized_func  # normalized_func is attribute value
        return result

    def convert(self, cls):
        if not CookbookRecipe.has(cls):
            CookbookRecipe.add(AuthenticRecipe(cls=cls))

        values = self.export()
        obj_params = {cls.LOCALIZE_RULES[k]: v for k, v in values.items() if k in cls.LOCALIZE_RULES}
        return cls(**obj_params)
