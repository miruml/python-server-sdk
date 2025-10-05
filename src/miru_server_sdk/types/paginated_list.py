# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaginatedList"]


class PaginatedList(BaseModel):
    has_more: bool
    """True if there are more items in the list to return.

    False if there are no more items to return.
    """

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    object: Literal["list"]

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    total_count: int
    """The total number of items in the list.

    By default the total count is not returned. The total count must be expanded
    (using expand[]=total_count) to get the total number of items in the list.
    """
