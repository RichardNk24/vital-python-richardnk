# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .client_facing_lab_test import ClientFacingLabTest
from .client_facing_order_details import ClientFacingOrderDetails
from .client_facing_order_event import ClientFacingOrderEvent
from .client_facing_patient_details_compatible import ClientFacingPatientDetailsCompatible
from .client_facing_physician import ClientFacingPhysician
from .order_top_level_status import OrderTopLevelStatus
from .patient_address_compatible import PatientAddressCompatible
from .shipping_address import ShippingAddress

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingOrder(pydantic.BaseModel):
    user_id: str = pydantic.Field(
        description="User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api."
    )
    id: str = pydantic.Field(description="The Vital Order ID")
    team_id: str = pydantic.Field(description="Your team id.")
    patient_details: typing.Optional[ClientFacingPatientDetailsCompatible]
    patient_address: typing.Optional[PatientAddressCompatible]
    lab_test: ClientFacingLabTest = pydantic.Field(description="The Vital Test associated with the order")
    details: ClientFacingOrderDetails
    sample_id: typing.Optional[str]
    notes: typing.Optional[str]
    created_at: dt.datetime = pydantic.Field(description="When your order was created")
    updated_at: dt.datetime = pydantic.Field(description="When your order was last updated.")
    events: typing.List[ClientFacingOrderEvent]
    status: typing.Optional[OrderTopLevelStatus]
    physician: typing.Optional[ClientFacingPhysician]
    health_insurance_id: typing.Optional[str]
    requisition_form_url: typing.Optional[str]
    priority: typing.Optional[bool] = pydantic.Field(
        description="Defines whether order is priority or not. For some labs, this refers to a STAT order."
    )
    shipping_details: typing.Optional[ShippingAddress]
    activate_by: typing.Optional[str]
    passthrough: typing.Optional[str]

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
