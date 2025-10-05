# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .paginated_list import PaginatedList

__all__ = ["ConfigInstanceListResponse"]


class ConfigInstanceListResponse(PaginatedList):
    data: List["ConfigInstance"]


from .config_instance import ConfigInstance
