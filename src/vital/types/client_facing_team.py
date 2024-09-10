# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .client_facing_api_key import ClientFacingApiKey
from .team_config import TeamConfig
from .delegated_flow_type import DelegatedFlowType
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ClientFacingTeam(UniversalBaseModel):
    """
    [Deprecated] GET /v2/team is in the process of being removed.
    Neither customers nor Dashboard should retrieve team settings and metadata directly.

    All must migrate to the Team endpoints of the Org Management API.
    """

    id: str
    org_id: str
    name: str
    svix_app_id: typing.Optional[str] = None
    client_id: typing.Optional[str] = None
    client_secret: typing.Optional[str] = None
    airtable_api_key: typing.Optional[str] = None
    airtable_base_id: typing.Optional[str] = None
    webhook_secret: typing.Optional[str] = None
    api_key: typing.Optional[str] = None
    api_keys: typing.Optional[typing.List[ClientFacingApiKey]] = None
    configuration: typing.Optional[TeamConfig] = None
    testkits_texts_enabled: bool
    lab_tests_patient_communication_enabled: bool
    lab_tests_patient_sms_communication_enabled: bool
    lab_tests_patient_email_communication_enabled: bool
    logo_url: typing.Optional[str] = None
    delegated_flow: DelegatedFlowType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
