# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .paginated_list import PaginatedList

__all__ = ["ConfigSchemaList"]


class ConfigSchemaList(PaginatedList):
    data: List["ConfigSchema"]


from .config_schema import ConfigSchema
