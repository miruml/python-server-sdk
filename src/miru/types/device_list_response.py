# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .device import Device
from .paginated_list import PaginatedList

__all__ = ["DeviceListResponse"]


class DeviceListResponse(PaginatedList):
    data: Optional[List[Device]] = None
