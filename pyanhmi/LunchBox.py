from collections import defaultdict
from typing import Tuple, Any, Optional, List, Union, overload, TypeVar, Dict, Type

from common.Config import CastingMode, ExportOrder
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create
from pyanhmi.Recipe.AuthenticRecipe import AuthenticRecipe
from pyanhmi.Recipe.Recipe import Recipe

T = TypeVar("T")


class LunchBox:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, data: dict, classes: type[T], recipes: Recipe, mode: CastingMode = None) -> None:
        ...

    @overload
    def __init__(self, data: dict, classes: List[type[T]], recipes: List[Recipe], mode: CastingMode = None) -> None:
        ...

    def __init__(self, data: Optional[dict] = None,
                 classes: Optional[Union[type[T], List[type[T]]]] = None,
                 recipes: Optional[Union[Recipe, List[Recipe]]] = None,
                 mode: Optional[CastingMode] = None) -> None:
        self.sources: Dict[Type, List[Tuple[int, Any]]] = defaultdict(list)
        self.obj_count = 0
        self.last_idx = 0
        for obj in create(data=data, classes=classes, recipes=recipes, mode=mode):
            self.add(obj)

    @property
    def is_item_idx_continuous(self):
        """
        Check whether the added items have been deleted or not
        If the item count != the last index -> there is object deleted -> return False
        :return:
        """
        return self.obj_count == self.last_idx

    @staticmethod
    def get_item_idx(item) -> int:
        """
        Get item's index
        :param item:
        :return:
        """
        return item[0]

    @staticmethod
    def get_item_obj(item) -> Any:
        """
        Get real object of item
        :param item:
        :return:
        """
        return item[1]

    def add(self, obj: Any) -> None:
        if not CookbookRecipe.has(type(obj)):
            CookbookRecipe.add(type(obj))
        self.sources[type(obj)].append((self.obj_count, obj))
        self.obj_count += 1
        self.last_idx += 1

    def get_latest_items_of_each_source(self) -> Dict[Type, Any]:
        """
        Get latest item in each source
        :return:
        """
        return {cls: objs[-1] for cls, objs in self.sources.items()}

    def get_latest_objs(self, *args):
        """
        Return the latest obj in each source
        Raise IndexError if one of cls is not in source
        :return:
        """
        if len(args) == 0:
            return tuple([LunchBox.get_item_obj(self.sources[obj_type][-1]) for obj_type in self.sources.keys()])
        elif len(args) == 1:
            return LunchBox.get_item_obj(self.sources[args[0]][-1])
        else:
            return tuple([LunchBox.get_item_obj(self.sources[obj_type][-1]) for obj_type in args])

    def get_fields_list(self):
        """
        Get all possible fields from all sources in lunchbox
        :return:
        """
        fields = set()
        for obj in self.get_latest_objs():
            recipe = CookbookRecipe.get(type(obj))
            for field, rule in recipe.ingredients.items():
                fields.add(rule.alias)
        return fields

    @staticmethod
    def _get_obj_by_idx_in_slice(sources_slice: list, obj_idx: int) -> Tuple[int, Any]:
        for cls_idx in range(0, len(sources_slice)):
            if LunchBox.get_item_idx(sources_slice[cls_idx]) == obj_idx:
                return cls_idx, sources_slice[cls_idx]
        return -1, None

    @staticmethod
    def _get_latest_obj_in_slice(sources_slice: list) -> Tuple[int, Any]:
        latest_obj = sources_slice[0]
        latest_idx = 0
        for idx in range(1, len(sources_slice)):
            if LunchBox.get_item_idx(sources_slice[idx]) > LunchBox.get_item_idx(latest_obj):
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
            if LunchBox.get_item_idx(sources_slice[cls_idx]) < LunchBox.get_item_idx(oldest_obj):
                oldest_obj = sources_slice[cls_idx]
                oldest_idx = cls_idx
        return oldest_idx, oldest_obj

    def get_all_objs(self) -> list:
        """
        Get all objects of all sources by ascending order
        :return:
        """
        objs_idx = [0] * len(self.sources)
        sources_values = list(self.sources.values())

        result = []
        for obj_idx in range(self.obj_count):
            sources_slice = [sources_values[source_idx][source_obj_idx] if source_obj_idx != -1 else (self.last_idx, None)
                             for source_idx, source_obj_idx in enumerate(objs_idx)]
            # oldest_idx, oldest_obj = self._get_obj_by_idx_in_slice(sources_slice, obj_idx) if self.is_item_idx_continuous \
            #     else self._get_oldest_obj_in_slice(sources_slice)
            oldest_idx, oldest_obj = self._get_obj_by_idx_in_slice(sources_slice, obj_idx)
            result.append(LunchBox.get_item_obj(oldest_obj))
            objs_idx[oldest_idx] += 1
            if objs_idx[oldest_idx] == len(sources_values[oldest_idx]):
                objs_idx[oldest_idx] = -1  # finish this source
        return result

    def export(self, target_normalize_fields=None, export_order: ExportOrder = ExportOrder.LIFO,
               is_override: bool = False):
        """
        check from the last added source (LIFO)
        :param target_normalize_fields:
        :param export_order:
        :param is_override:
        :return:
        """

        def is_done():
            if not is_override:
                # if not is_override then continue checking other source
                return False
            if target_normalize_fields == set(result.keys()):
                # stop checking if all desired fields are collected
                return True
            return False

        def get_field_val():
            normalized_func = source.__getattribute__(rule.getter_func)
            if hasattr(normalized_func, "__call__"):
                return normalized_func()  # call method
            else:
                return normalized_func  # normalized_func is attribute value

        all_fields = self.get_fields_list()
        target_normalize_fields = target_normalize_fields or all_fields
        target_normalize_fields = all_fields.intersection(set(target_normalize_fields))  # remove undesired fields

        all_objs = self.get_all_objs()
        sources = all_objs if export_order == ExportOrder.FIFO else reversed(all_objs)

        not_default_values = set()  # used to mark all assigned not-default value
        result = {}
        for source in sources:
            if is_done():
                break
            recipe = CookbookRecipe.get(type(source))

            for field, rule in recipe.ingredients.items():
                if rule.alias not in target_normalize_fields:
                    continue
                if is_override and rule.alias in result:
                    # keep using the latest added obj (lifo) or first added obj (fifo)
                    continue
                if rule.alias in not_default_values:
                    # the not-default value is added to result already
                    continue
                new_val = get_field_val()

                if new_val != rule.default:
                    not_default_values.add(rule.alias)

                result[rule.alias] = new_val
        return result

    def convert(self, cls, export_order: ExportOrder = ExportOrder.LIFO, is_override: bool = False):
        """
        create new object based on values in lunchbox
        :param cls:
        :param export_order:
        :param is_override:
        :return:
        """
        if not CookbookRecipe.has(cls):
            CookbookRecipe.add(cls)
        export_values = self.export(export_order=export_order, is_override=is_override)
        alias_mapping = {field.alias: field_name for field_name, field in CookbookRecipe.get(cls).ingredients.items()}
        obj_params = {alias_mapping[alias]: val for alias, val in export_values.items() if alias in alias_mapping}
        return cls(**obj_params)
