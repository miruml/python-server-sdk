# File generated from our OpenAPI spec by Stainless.
# See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import cast

from svix.webhooks import (
    Webhook as SvixWebhook,
    WebhookVerificationError as SvixWebhookVerificationError,
)

from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.unwrap_webhook_event import UnwrapWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]

Webhook = SvixWebhook
WebhookVerificationError = SvixWebhookVerificationError


class CallbackVerificationError(WebhookVerificationError):
    """Alias for WebhookVerificationError for backward compatibility"""
    pass


class WebhooksResource(SyncAPIResource):
    def unwrap(self, payload: str) -> UnwrapWebhookEvent:
        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooksResource(AsyncAPIResource):
    def unwrap(self, payload: str) -> UnwrapWebhookEvent:
        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )
