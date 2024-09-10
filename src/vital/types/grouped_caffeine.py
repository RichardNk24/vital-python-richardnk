# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .client_facing_source import ClientFacingSource
import typing
from .client_facing_caffeine_timeseries import ClientFacingCaffeineTimeseries
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GroupedCaffeine(UniversalBaseModel):
    source: ClientFacingSource
    data: typing.List[ClientFacingCaffeineTimeseries]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
