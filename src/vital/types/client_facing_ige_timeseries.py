# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientFacingIgeTimeseries(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated
    """

    timezone_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time zone UTC offset in seconds. Positive offset indicates east of UTC; negative offset indicates west of UTC; and null indicates the time zone information is unavailable at source.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reading type of the measurement. This is applicable only to Cholesterol, IGG, IGE and InsulinInjection.
    """

    unit: str = pydantic.Field()
    """
    Measured in FSU.
    """

    timestamp: str = pydantic.Field()
    """
    The timestamp of the measurement.
    """

    value: float = pydantic.Field()
    """
    The value of the measurement.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
