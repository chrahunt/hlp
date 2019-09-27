import importlib
import pkgutil
import sys

from .typing import MYPY_RUNNING

if MYPY_RUNNING:
    from typing import Any, Iterable, Iterator, List, Optional, Tuple


PY2 = sys.version_info < (2,)


def sequences(iterable):
    # type: (Iterable) -> Iterator[List[str]]
    items = []
    for item in iterable:
        items.append(item)
        yield list(items)


def import_longest_module(spec):
    # type: (str) -> Tuple[Any, str]
    module_name = spec
    parts = spec.split(".")

    for seq in reversed(list(sequences(parts))):
        module_name = ".".join(seq)
        try:
            last = importlib.import_module(module_name)
        except ImportError:
            pass
        else:
            break
    else:
        raise ImportError(module_name)

    leftover = parts[len(seq) :]
    return last, ".".join(leftover)


def getattr_recursive(o, attrs):
    # type: (Any, List[str]) -> Any
    for attr in attrs:
        o = getattr(o, attr)
    return o


def py3_iter_modules(path):
    # type: (Optional[str]) -> Iterator[Tuple[..., str, bool]]
    for info in pkgutil.iter_modules(path):
        yield info, info.name, info.ispkg


def iter_modules(path):
    # type: (Optional[str]) -> Iterator[Tuple[..., str, bool]]
    if PY2:
        return pkgutil.iter_modules(path)
    return py3_iter_modules(path)


def module_names(path):
    # type: (Optional[str]) -> Iterator[str]
    for _, name, _ in iter_modules(path):
        yield name


def children(name):
    """Given a name, get the available children.

    Children can be members (for a module) or members and contained modules
    (for a package).
    """
    pass


def autocomplete(current):
    """
    Given the current input, retrieve the autocomplete entries, like:

    1. If a complete name followed by a '.', then the children of the name
    2. if a complete name followed by a '.' and some text, then the children
       starting with that text
    3. if an incomplete name, then the available modules

    Names should include '.'-suffixed version, for modules and packages.
    """


def main():
    query = sys.argv[1]
    obj, attr_spec = import_longest_module(query)
    if attr_spec:
        obj = getattr_recursive(obj, attr_spec.split("."))
    help(obj)
