# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .paginated_list import PaginatedList
from .config_instance import ConfigInstance

__all__ = ["ConfigInstanceListResponse"]


class ConfigInstanceListResponse(PaginatedList):
    data: List[ConfigInstance]
