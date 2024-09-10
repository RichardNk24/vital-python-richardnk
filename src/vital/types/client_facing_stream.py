# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .client_facing_stream_cadence import ClientFacingStreamCadence
import pydantic
from .client_facing_stream_altitude import ClientFacingStreamAltitude
from .client_facing_stream_velocity_smooth import ClientFacingStreamVelocitySmooth
from .client_facing_stream_heartrate import ClientFacingStreamHeartrate
from .client_facing_stream_lat import ClientFacingStreamLat
from .client_facing_stream_lng import ClientFacingStreamLng
from .client_facing_stream_distance import ClientFacingStreamDistance
from .client_facing_stream_power import ClientFacingStreamPower
from .client_facing_stream_resistance import ClientFacingStreamResistance
from .client_facing_stream_temperature import ClientFacingStreamTemperature
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientFacingStream(UniversalBaseModel):
    cadence: typing.Optional[ClientFacingStreamCadence] = pydantic.Field(default=None)
    """
    RPM for cycling, Steps per minute for running
    """

    time: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Corresponding time stamp in unix time for datapoint
    """

    altitude: typing.Optional[ClientFacingStreamAltitude] = pydantic.Field(default=None)
    """
    Data points for altitude
    """

    velocity_smooth: typing.Optional[ClientFacingStreamVelocitySmooth] = pydantic.Field(default=None)
    """
    Velocity in m/s
    """

    heartrate: typing.Optional[ClientFacingStreamHeartrate] = pydantic.Field(default=None)
    """
    Heart rate in bpm
    """

    lat: typing.Optional[ClientFacingStreamLat] = pydantic.Field(default=None)
    """
    Latitude for data point
    """

    lng: typing.Optional[ClientFacingStreamLng] = pydantic.Field(default=None)
    """
    Longitude for data point
    """

    distance: typing.Optional[ClientFacingStreamDistance] = pydantic.Field(default=None)
    """
    Cumulated distance for exercise
    """

    power: typing.Optional[ClientFacingStreamPower] = pydantic.Field(default=None)
    """
    Power in watts
    """

    resistance: typing.Optional[ClientFacingStreamResistance] = pydantic.Field(default=None)
    """
    Resistance on bike
    """

    temperature: typing.Optional[ClientFacingStreamTemperature] = pydantic.Field(default=None)
    """
    Temperature stream measured by device in Celsius
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
