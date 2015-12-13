from json import loads
from types import FunctionType


def filter_pt1(item):
    return item


def filter_pt2(item):
    if "red" in item.values():
        return None

    return item


def solve(source: str, obj_hook: FunctionType=filter_pt1) -> int:
    items = loads(source, object_hook=obj_hook)

    return recursive_add(items)


def add_total(obj, total: int, init: int=None) -> int:
    if isinstance(obj, (int, float)):
        return total + obj

    return total


def recursive_add(items: iter, total: int=0) -> int:
    if isinstance(items, dict):
        items = items.values()

    for item in items:
        if isinstance(item, (list, dict)):
            total = recursive_add(item, total)

        else:
            total = add_total(item, total)

    return total
