from .typing import MYPY_RUNNING

if MYPY_RUNNING:
    from typing import Any, Iterable, Iterator, List


def getattr_recursive(o, attrs):
    # type: (Any, List[str]) -> Any
    for attr in attrs:
        o = getattr(o, attr)
    return o


def sequences(iterable):
    # type: (Iterable) -> Iterator[List[str]]
    """Returns sequences of increasing length from the start of the given iterable.
    """
    items = []
    for item in iterable:
        items.append(item)
        yield list(items)
