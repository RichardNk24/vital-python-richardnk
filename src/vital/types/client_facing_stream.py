# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .client_facing_stream_altitude import ClientFacingStreamAltitude
from .client_facing_stream_cadence import ClientFacingStreamCadence
from .client_facing_stream_distance import ClientFacingStreamDistance
from .client_facing_stream_heartrate import ClientFacingStreamHeartrate
from .client_facing_stream_lat import ClientFacingStreamLat
from .client_facing_stream_lng import ClientFacingStreamLng
from .client_facing_stream_power import ClientFacingStreamPower
from .client_facing_stream_resistance import ClientFacingStreamResistance
from .client_facing_stream_velocity_smooth import ClientFacingStreamVelocitySmooth

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingStream(pydantic.BaseModel):
    cadence: typing.Optional[ClientFacingStreamCadence] = pydantic.Field(
        description="RPM for cycling, Steps per minute for running"
    )
    time: typing.Optional[typing.List[int]]
    altitude: typing.Optional[ClientFacingStreamAltitude] = pydantic.Field(description="Data points for altitude")
    velocity_smooth: typing.Optional[ClientFacingStreamVelocitySmooth] = pydantic.Field(description="Velocity in m/s")
    heartrate: typing.Optional[ClientFacingStreamHeartrate] = pydantic.Field(description="Heart rate in bpm")
    lat: typing.Optional[ClientFacingStreamLat] = pydantic.Field(description="Latitude for data point")
    lng: typing.Optional[ClientFacingStreamLng] = pydantic.Field(description="Longitude for data point")
    distance: typing.Optional[ClientFacingStreamDistance] = pydantic.Field(
        description="Cumulated distance for exercise"
    )
    power: typing.Optional[ClientFacingStreamPower] = pydantic.Field(description="Power in watts")
    resistance: typing.Optional[ClientFacingStreamResistance] = pydantic.Field(description="Resistance on bike")

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
