# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientFacingShipment(UniversalBaseModel):
    """
    Schema for a Shipment in the client facing API.

    To be used as part of a ClientFacingTestkitOrder.
    """

    id: str = pydantic.Field()
    """
    The Vital Shipment ID
    """

    outbound_tracking_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tracking number for delivery to customer
    """

    outbound_tracking_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tracking url for delivery to customer
    """

    inbound_tracking_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tracking number for delivery to lab
    """

    inbound_tracking_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tracking url for delivery to lab
    """

    outbound_courier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Courier used for delivery to customer
    """

    inbound_courier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Courier used for delivery to lab
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes associated to the Vital shipment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
