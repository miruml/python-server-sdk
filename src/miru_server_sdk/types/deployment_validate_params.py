# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DeploymentValidateParams", "ConfigInstance", "ConfigInstanceParameter"]


class DeploymentValidateParams(TypedDict, total=False):
    config_instances: Required[Iterable[ConfigInstance]]
    """The config instance errors for this deployment."""

    is_valid: Required[bool]
    """Whether the deployment is valid.

    If invalid, the deployment is immediately archived and marked as 'failed'.
    """

    message: Required[str]
    """A message displayed on the deployment level in the UI."""


class ConfigInstanceParameter(TypedDict, total=False):
    message: Required[str]
    """An error message displayed for an individual parameter."""

    path: Required[SequenceNotStr[str]]
    """The path to the parameter that is invalid."""


class ConfigInstance(TypedDict, total=False):
    id: Required[str]
    """ID of the config instance."""

    message: Required[str]
    """A message displayed on the config instance level in the UI."""

    parameters: Required[Iterable[ConfigInstanceParameter]]
    """The parameter errors for this config instance."""
