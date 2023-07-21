r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.insights.v1.room.participant import ParticipantList


class RoomInstance(InstanceResource):
    class Codec(object):
        VP8 = "VP8"
        H264 = "H264"
        VP9 = "VP9"

    class CreatedMethod(object):
        SDK = "sdk"
        AD_HOC = "ad_hoc"
        API = "api"

    class EdgeLocation(object):
        ASHBURN = "ashburn"
        DUBLIN = "dublin"
        FRANKFURT = "frankfurt"
        SINGAPORE = "singapore"
        SYDNEY = "sydney"
        SAO_PAULO = "sao_paulo"
        ROAMING = "roaming"
        UMATILLA = "umatilla"
        TOKYO = "tokyo"

    class EndReason(object):
        ROOM_ENDED_VIA_API = "room_ended_via_api"
        TIMEOUT = "timeout"

    class ProcessingState(object):
        COMPLETE = "complete"
        IN_PROGRESS = "in_progress"

    class RoomStatus(object):
        IN_PROGRESS = "in_progress"
        COMPLETED = "completed"

    class RoomType(object):
        GO = "go"
        PEER_TO_PEER = "peer_to_peer"
        GROUP = "group"
        GROUP_SMALL = "group_small"

    class TwilioRealm(object):
        US1 = "us1"
        US2 = "us2"
        AU1 = "au1"
        BR1 = "br1"
        IE1 = "ie1"
        JP1 = "jp1"
        SG1 = "sg1"
        IN1 = "in1"
        DE1 = "de1"
        GLL = "gll"

    """
    :ivar account_sid: Account SID associated with this room.
    :ivar room_sid: Unique identifier for the room.
    :ivar room_name: Room friendly name.
    :ivar create_time: Creation time of the room.
    :ivar end_time: End time for the room.
    :ivar room_type: 
    :ivar room_status: 
    :ivar status_callback: Webhook provided for status callbacks.
    :ivar status_callback_method: HTTP method provided for status callback URL.
    :ivar created_method: 
    :ivar end_reason: 
    :ivar max_participants: Max number of total participants allowed by the application settings.
    :ivar unique_participants: Number of participants. May include duplicate identities for participants who left and rejoined.
    :ivar unique_participant_identities: Unique number of participant identities.
    :ivar concurrent_participants: Actual number of concurrent participants.
    :ivar max_concurrent_participants: Maximum number of participants allowed in the room at the same time allowed by the application settings.
    :ivar codecs: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
    :ivar media_region: 
    :ivar duration_sec: Total room duration from create time to end time.
    :ivar total_participant_duration_sec: Combined amount of participant time in the room.
    :ivar total_recording_duration_sec: Combined amount of recorded seconds for participants in the room.
    :ivar processing_state: 
    :ivar recording_enabled: Boolean indicating if recording is enabled for the room.
    :ivar edge_location: 
    :ivar url: URL for the room resource.
    :ivar links: Room subresources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], room_sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.room_sid: Optional[str] = payload.get("room_sid")
        self.room_name: Optional[str] = payload.get("room_name")
        self.create_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("create_time")
        )
        self.end_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("end_time")
        )
        self.room_type: Optional["RoomInstance.RoomType"] = payload.get("room_type")
        self.room_status: Optional["RoomInstance.RoomStatus"] = payload.get(
            "room_status"
        )
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.created_method: Optional["RoomInstance.CreatedMethod"] = payload.get(
            "created_method"
        )
        self.end_reason: Optional["RoomInstance.EndReason"] = payload.get("end_reason")
        self.max_participants: Optional[int] = deserialize.integer(
            payload.get("max_participants")
        )
        self.unique_participants: Optional[int] = deserialize.integer(
            payload.get("unique_participants")
        )
        self.unique_participant_identities: Optional[int] = deserialize.integer(
            payload.get("unique_participant_identities")
        )
        self.concurrent_participants: Optional[int] = deserialize.integer(
            payload.get("concurrent_participants")
        )
        self.max_concurrent_participants: Optional[int] = deserialize.integer(
            payload.get("max_concurrent_participants")
        )
        self.codecs: Optional[List["RoomInstance.Codec"]] = payload.get("codecs")
        self.media_region: Optional["RoomInstance.TwilioRealm"] = payload.get(
            "media_region"
        )
        self.duration_sec: Optional[int] = payload.get("duration_sec")
        self.total_participant_duration_sec: Optional[int] = payload.get(
            "total_participant_duration_sec"
        )
        self.total_recording_duration_sec: Optional[int] = payload.get(
            "total_recording_duration_sec"
        )
        self.processing_state: Optional["RoomInstance.ProcessingState"] = payload.get(
            "processing_state"
        )
        self.recording_enabled: Optional[bool] = payload.get("recording_enabled")
        self.edge_location: Optional["RoomInstance.EdgeLocation"] = payload.get(
            "edge_location"
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "room_sid": room_sid or self.room_sid,
        }
        self._context: Optional[RoomContext] = None

    @property
    def _proxy(self) -> "RoomContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoomContext for this RoomInstance
        """
        if self._context is None:
            self._context = RoomContext(
                self._version,
                room_sid=self._solution["room_sid"],
            )
        return self._context

    def fetch(self) -> "RoomInstance":
        """
        Fetch the RoomInstance


        :returns: The fetched RoomInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RoomInstance":
        """
        Asynchronous coroutine to fetch the RoomInstance


        :returns: The fetched RoomInstance
        """
        return await self._proxy.fetch_async()

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        return self._proxy.participants

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.RoomInstance {}>".format(context)


class RoomContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the RoomContext

        :param version: Version that contains the resource
        :param room_sid: The SID of the Room resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
        }
        self._uri = "/Video/Rooms/{room_sid}".format(**self._solution)

        self._participants: Optional[ParticipantList] = None

    def fetch(self) -> RoomInstance:
        """
        Fetch the RoomInstance


        :returns: The fetched RoomInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RoomInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
        )

    async def fetch_async(self) -> RoomInstance:
        """
        Asynchronous coroutine to fetch the RoomInstance


        :returns: The fetched RoomInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RoomInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
        )

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                self._solution["room_sid"],
            )
        return self._participants

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.RoomContext {}>".format(context)


class RoomPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> RoomInstance:
        """
        Build an instance of RoomInstance

        :param payload: Payload response from the API
        """
        return RoomInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.RoomPage>"


class RoomList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the RoomList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Video/Rooms"

    def stream(
        self,
        room_type: Union[List["RoomInstance.RoomType"], object] = values.unset,
        codec: Union[List["RoomInstance.Codec"], object] = values.unset,
        room_name: Union[str, object] = values.unset,
        created_after: Union[datetime, object] = values.unset,
        created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[RoomInstance]:
        """
        Streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;RoomInstance.RoomType&quot;] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param List[&quot;RoomInstance.Codec&quot;] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        room_type: Union[List["RoomInstance.RoomType"], object] = values.unset,
        codec: Union[List["RoomInstance.Codec"], object] = values.unset,
        room_name: Union[str, object] = values.unset,
        created_after: Union[datetime, object] = values.unset,
        created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[RoomInstance]:
        """
        Asynchronously streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;RoomInstance.RoomType&quot;] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param List[&quot;RoomInstance.Codec&quot;] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        room_type: Union[List["RoomInstance.RoomType"], object] = values.unset,
        codec: Union[List["RoomInstance.Codec"], object] = values.unset,
        room_name: Union[str, object] = values.unset,
        created_after: Union[datetime, object] = values.unset,
        created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RoomInstance]:
        """
        Lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;RoomInstance.RoomType&quot;] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param List[&quot;RoomInstance.Codec&quot;] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                room_type=room_type,
                codec=codec,
                room_name=room_name,
                created_after=created_after,
                created_before=created_before,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        room_type: Union[List["RoomInstance.RoomType"], object] = values.unset,
        codec: Union[List["RoomInstance.Codec"], object] = values.unset,
        room_name: Union[str, object] = values.unset,
        created_after: Union[datetime, object] = values.unset,
        created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RoomInstance]:
        """
        Asynchronously lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;RoomInstance.RoomType&quot;] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param List[&quot;RoomInstance.Codec&quot;] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                room_type=room_type,
                codec=codec,
                room_name=room_name,
                created_after=created_after,
                created_before=created_before,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        room_type: Union[List["RoomInstance.RoomType"], object] = values.unset,
        codec: Union[List["RoomInstance.Codec"], object] = values.unset,
        room_name: Union[str, object] = values.unset,
        created_after: Union[datetime, object] = values.unset,
        created_before: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RoomPage:
        """
        Retrieve a single page of RoomInstance records from the API.
        Request is executed immediately

        :param room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param room_name: Room friendly name.
        :param created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        """
        data = values.of(
            {
                "RoomType": serialize.map(room_type, lambda e: e),
                "Codec": serialize.map(codec, lambda e: e),
                "RoomName": room_name,
                "CreatedAfter": serialize.iso8601_datetime(created_after),
                "CreatedBefore": serialize.iso8601_datetime(created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RoomPage(self._version, response)

    async def page_async(
        self,
        room_type: Union[List["RoomInstance.RoomType"], object] = values.unset,
        codec: Union[List["RoomInstance.Codec"], object] = values.unset,
        room_name: Union[str, object] = values.unset,
        created_after: Union[datetime, object] = values.unset,
        created_before: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RoomPage:
        """
        Asynchronously retrieve a single page of RoomInstance records from the API.
        Request is executed immediately

        :param room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param room_name: Room friendly name.
        :param created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        """
        data = values.of(
            {
                "RoomType": serialize.map(room_type, lambda e: e),
                "Codec": serialize.map(codec, lambda e: e),
                "RoomName": room_name,
                "CreatedAfter": serialize.iso8601_datetime(created_after),
                "CreatedBefore": serialize.iso8601_datetime(created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return RoomPage(self._version, response)

    def get_page(self, target_url: str) -> RoomPage:
        """
        Retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RoomPage(self._version, response)

    async def get_page_async(self, target_url: str) -> RoomPage:
        """
        Asynchronously retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RoomPage(self._version, response)

    def get(self, room_sid: str) -> RoomContext:
        """
        Constructs a RoomContext

        :param room_sid: The SID of the Room resource.
        """
        return RoomContext(self._version, room_sid=room_sid)

    def __call__(self, room_sid: str) -> RoomContext:
        """
        Constructs a RoomContext

        :param room_sid: The SID of the Room resource.
        """
        return RoomContext(self._version, room_sid=room_sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.RoomList>"
