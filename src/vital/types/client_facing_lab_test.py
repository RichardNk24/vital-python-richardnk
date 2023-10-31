# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .client_facing_lab import ClientFacingLab
from .client_facing_marker import ClientFacingMarker
from .lab_test_collection_method import LabTestCollectionMethod
from .lab_test_sample_type import LabTestSampleType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingLabTest(pydantic.BaseModel):
    id: str
    slug: str
    name: str
    sample_type: LabTestSampleType
    method: LabTestCollectionMethod
    price: float
    is_active: bool
    fasting: typing.Optional[bool] = pydantic.Field(
        description="Defines whether a lab test requires fasting. Only available for Labcorp."
    )
    lab: typing.Optional[ClientFacingLab]
    markers: typing.Optional[typing.List[ClientFacingMarker]]
    is_delegated: typing.Optional[bool] = pydantic.Field(
        description="Denotes whether a lab test requires using non-Vital physician networks. If it does then it's delegated - no otherwise."
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
