# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .energy import Energy
from .macros import Macros
from .micros import Micros
from .client_facing_food import ClientFacingFood
from .client_facing_source import ClientFacingSource
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MealInDbBaseClientFacingSource(UniversalBaseModel):
    id: str
    user_id: str
    priority_id: int
    source_id: int
    provider_id: str
    timestamp: str
    name: str
    energy: typing.Optional[Energy] = None
    macros: typing.Optional[Macros] = None
    micros: typing.Optional[Micros] = None
    data: typing.Optional[typing.Dict[str, ClientFacingFood]] = None
    source: ClientFacingSource
    created_at: str
    updated_at: str
    source_app_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
