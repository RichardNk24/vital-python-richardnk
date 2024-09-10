# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientFacingSource(UniversalBaseModel):
    """
    Source summarizes where a sample or a summary is sourced from.
    At minimum, the source provider is always included.
    """

    provider: str = pydantic.Field()
    """
    Provider slug. e.g., `oura`, `fitbit`, `garmin`.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the data source (app or device) by which the summary or the timeseries data were recorded. This defaults to `unknown` when Vital cannot extract or infer that information
    """

    app_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the app which recorded this summary. This is only applicable to multi-source providers like Apple Health and Android Health Connect.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated. Subject to removal after 1 Jan 2024.
    """

    slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated. Use `provider` instead. Subject to removal after 1 Jan 2024.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated. Subject to removal after 1 Jan 2024.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
