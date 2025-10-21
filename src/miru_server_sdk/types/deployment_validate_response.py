# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .deployment import Deployment

__all__ = ["DeploymentValidateResponse"]


class DeploymentValidateResponse(BaseModel):
    deployment: Deployment

    effect: Literal["none", "stage", "deploy", "reject", "void"]
    """The effect of the validation."""

    message: str
    """A message explaining the validation effect."""
