# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .release import Release
from .paginated_list import PaginatedList

__all__ = ["ReleaseListResponse"]


class ReleaseListResponse(PaginatedList):
    data: List[Release]
