# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .base_device import BaseDevice
from .paginated_list import PaginatedList

__all__ = ["DeviceListResponse"]


class DeviceListResponse(PaginatedList):
    data: Optional[List[BaseDevice]] = None
