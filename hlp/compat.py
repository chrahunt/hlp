import pkgutil
import sys

from .typing import MYPY_RUNNING

if MYPY_RUNNING:
    from typing import Any, Iterator, Optional, Tuple


PY2 = sys.version_info < (3,)


if PY2:

    def iter_modules(path=None):
        # type: (Optional[str]) -> Iterator[Tuple[Any, str, bool]]
        return pkgutil.iter_modules(path)


else:

    def iter_modules(path=None):
        # type: (Optional[str]) -> Iterator[Tuple[Any, str, bool]]
        for info in pkgutil.iter_modules(path):
            yield info, info.name, info.ispkg
