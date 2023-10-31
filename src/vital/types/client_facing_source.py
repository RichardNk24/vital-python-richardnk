# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingSource(pydantic.BaseModel):
    """
    Source summarizes where a sample or a summary is sourced from.
    At minimum, the source provider is always included.
    """

    provider: str = pydantic.Field(description="Provider slug. e.g., `oura`, `fitbit`, `garmin`.")
    type: typing.Optional[str] = pydantic.Field(
        description="The type of the data source (app or device) by which the summary or the timeseries data were recorded. This defaults to `unknown` when Vital cannot extract or infer that information"
    )
    app_id: typing.Optional[str] = pydantic.Field(
        description="The identifier of the app which recorded this summary. This is only applicable to multi-source providers like Apple Health and Android Health Connect."
    )
    name: str = pydantic.Field(description="Deprecated. Subject to removal after 1 Jan 2024.")
    slug: str = pydantic.Field(description="Deprecated. Use `provider` instead. Subject to removal after 1 Jan 2024.")
    logo: str = pydantic.Field(description="Deprecated. Subject to removal after 1 Jan 2024.")

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
