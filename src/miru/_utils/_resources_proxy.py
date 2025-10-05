from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `miru.resources` module.

    This is used so that we can lazily import `miru.resources` only when
    needed *and* so that users can just import `miru` and reference `miru.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("miru.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
