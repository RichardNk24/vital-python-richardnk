# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .phlebotomy_area_info import PhlebotomyAreaInfo
import typing
from .psc_area_info import PscAreaInfo
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AreaInfo(UniversalBaseModel):
    zip_code: str
    phlebotomy: PhlebotomyAreaInfo
    central_labs: typing.Dict[str, PscAreaInfo]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
