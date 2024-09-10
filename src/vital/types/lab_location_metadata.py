# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class LabLocationMetadata(UniversalBaseModel):
    name: str
    state: str
    city: str
    zip_code: str
    first_line: str
    second_line: typing.Optional[str] = None
    phone_number: typing.Optional[str] = None
    fax_number: typing.Optional[str] = None
    hours: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
