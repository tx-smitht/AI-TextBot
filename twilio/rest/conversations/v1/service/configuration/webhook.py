r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class WebhookInstance(InstanceResource):
    class Method(object):
        GET = "GET"
        POST = "POST"

    """
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this service.
    :ivar chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
    :ivar pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
    :ivar post_webhook_url: The absolute url the post-event webhook request should be sent to.
    :ivar filters: The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.
    :ivar method: 
    :ivar url: An absolute API resource URL for this webhook.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], chat_service_sid: str
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.chat_service_sid: Optional[str] = payload.get("chat_service_sid")
        self.pre_webhook_url: Optional[str] = payload.get("pre_webhook_url")
        self.post_webhook_url: Optional[str] = payload.get("post_webhook_url")
        self.filters: Optional[List[str]] = payload.get("filters")
        self.method: Optional["WebhookInstance.Method"] = payload.get("method")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "chat_service_sid": chat_service_sid,
        }
        self._context: Optional[WebhookContext] = None

    @property
    def _proxy(self) -> "WebhookContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WebhookContext for this WebhookInstance
        """
        if self._context is None:
            self._context = WebhookContext(
                self._version,
                chat_service_sid=self._solution["chat_service_sid"],
            )
        return self._context

    def fetch(self) -> "WebhookInstance":
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "WebhookInstance":
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        method: Union[str, object] = values.unset,
    ) -> "WebhookInstance":
        """
        Update the WebhookInstance

        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param filters: The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.
        :param method: The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.

        :returns: The updated WebhookInstance
        """
        return self._proxy.update(
            pre_webhook_url=pre_webhook_url,
            post_webhook_url=post_webhook_url,
            filters=filters,
            method=method,
        )

    async def update_async(
        self,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        method: Union[str, object] = values.unset,
    ) -> "WebhookInstance":
        """
        Asynchronous coroutine to update the WebhookInstance

        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param filters: The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.
        :param method: The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.

        :returns: The updated WebhookInstance
        """
        return await self._proxy.update_async(
            pre_webhook_url=pre_webhook_url,
            post_webhook_url=post_webhook_url,
            filters=filters,
            method=method,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.WebhookInstance {}>".format(context)


class WebhookContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the WebhookContext

        :param version: Version that contains the resource
        :param chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
        }
        self._uri = "/Services/{chat_service_sid}/Configuration/Webhooks".format(
            **self._solution
        )

    def fetch(self) -> WebhookInstance:
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
        )

    async def fetch_async(self) -> WebhookInstance:
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
        )

    def update(
        self,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        method: Union[str, object] = values.unset,
    ) -> WebhookInstance:
        """
        Update the WebhookInstance

        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param filters: The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.
        :param method: The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "PreWebhookUrl": pre_webhook_url,
                "PostWebhookUrl": post_webhook_url,
                "Filters": serialize.map(filters, lambda e: e),
                "Method": method,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    async def update_async(
        self,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        method: Union[str, object] = values.unset,
    ) -> WebhookInstance:
        """
        Asynchronous coroutine to update the WebhookInstance

        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param filters: The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.
        :param method: The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "PreWebhookUrl": pre_webhook_url,
                "PostWebhookUrl": post_webhook_url,
                "Filters": serialize.map(filters, lambda e: e),
                "Method": method,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.WebhookContext {}>".format(context)


class WebhookList(ListResource):
    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the WebhookList

        :param version: Version that contains the resource
        :param chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
        }

    def get(self) -> WebhookContext:
        """
        Constructs a WebhookContext

        """
        return WebhookContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __call__(self) -> WebhookContext:
        """
        Constructs a WebhookContext

        """
        return WebhookContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.WebhookList>"
