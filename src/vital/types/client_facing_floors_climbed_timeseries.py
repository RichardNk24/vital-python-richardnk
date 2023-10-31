# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingFloorsClimbedTimeseries(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(description="Deprecated")
    timezone_offset: typing.Optional[int] = pydantic.Field(
        description="Time zone UTC offset in seconds. Positive offset indicates east of UTC; negative offset indicates west of UTC; and null indicates the time zone information is unavailable at source."
    )
    type: typing.Optional[str] = pydantic.Field(
        description="The reading type of the measurement. This is applicable only to Cholesterol, IGG and IGE."
    )
    unit: typing_extensions.Literal["count"]
    timestamp: dt.datetime = pydantic.Field(description="The timestamp of the measurement.")
    value: float = pydantic.Field(description="Number of floors climbed at the time or interval::count")

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
