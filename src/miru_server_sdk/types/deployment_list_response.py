# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .deployment import Deployment
from .paginated_list import PaginatedList

__all__ = ["DeploymentListResponse"]


class DeploymentListResponse(PaginatedList):
    data: List[Deployment]
