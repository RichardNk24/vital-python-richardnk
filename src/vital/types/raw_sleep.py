# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .sleep_v_2_in_db import SleepV2InDb
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class RawSleep(UniversalBaseModel):
    sleep: typing.List[SleepV2InDb]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
