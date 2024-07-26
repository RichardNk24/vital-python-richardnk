# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class LinkTokenExchangeResponse(pydantic.BaseModel):
    link_token: str = pydantic.Field(
        description="A short-lived Vital Link token for your Custom Link Widget to communicate with the Vital API."
    )
    link_web_url: str = pydantic.Field(
        description="The web browser link to launch the default Vital Link experience. If you requested the token for one specific provider, the link would redirect directly to the provider authentication flow. Otherwise, the user would be presented with a list of providers based on your team and token configurations."
    )

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
