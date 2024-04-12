# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .connected_source_client_facing import ConnectedSourceClientFacing
from .fallback_birth_date import FallbackBirthDate
from .fallback_time_zone import FallbackTimeZone

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingUser(pydantic.BaseModel):
    user_id: str = pydantic.Field(
        description="User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api."
    )
    team_id: str = pydantic.Field(description="Your team id.")
    client_user_id: str = pydantic.Field(
        description="A unique ID representing the end user. Typically this will be a user ID from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id."
    )
    created_on: dt.datetime = pydantic.Field(description="When your item is created")
    connected_sources: typing.List[ConnectedSourceClientFacing] = pydantic.Field(
        description="A list of the users connected sources."
    )
    fallback_time_zone: typing.Optional[FallbackTimeZone] = pydantic.Field(
        description=(
            "    Fallback time zone of the user, in the form of a valid IANA tzdatabase identifier (e.g., `Europe/London` or `America/Los_Angeles`).\n"
            "    Used when pulling data from sources that are completely time zone agnostic (e.g., all time is relative to UTC clock, without any time zone attributions on data points).\n"
        )
    )
    fallback_birth_date: typing.Optional[FallbackBirthDate] = pydantic.Field(
        description="Fallback date of birth of the user, in YYYY-mm-dd format. Used for calculating max heartrate for providers that don not provide users' age."
    )
    ingestion_start: typing.Optional[str] = pydantic.Field(
        description="Starting bound for user data ingestion. Data older than this date will not be ingested."
    )
    ingestion_end: typing.Optional[str] = pydantic.Field(
        description="Ending bound for user data ingestion. Data newer than this date will not be ingested and the connection deregistered."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
