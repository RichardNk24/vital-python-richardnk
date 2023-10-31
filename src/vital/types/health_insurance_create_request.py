# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .health_insurance_create_request_back_image import HealthInsuranceCreateRequestBackImage
from .health_insurance_create_request_front_image import HealthInsuranceCreateRequestFrontImage
from .health_insurance_create_request_patient_signature_image import HealthInsuranceCreateRequestPatientSignatureImage
from .person_details import PersonDetails
from .responsible_relationship import ResponsibleRelationship

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class HealthInsuranceCreateRequest(pydantic.BaseModel):
    front_image: typing.Optional[HealthInsuranceCreateRequestFrontImage] = pydantic.Field(
        description="An image of the front of the patient insurance card."
    )
    back_image: typing.Optional[HealthInsuranceCreateRequestBackImage] = pydantic.Field(
        description="An image of the back of the patient insurance card."
    )
    patient_signature_image: typing.Optional[HealthInsuranceCreateRequestPatientSignatureImage] = pydantic.Field(
        description="An image of the patient signature for health insurance billing."
    )
    subjective: typing.Optional[str] = pydantic.Field(
        description="Textual description of what are the patient symptoms and attempted treatments."
    )
    assessment_plan: typing.Optional[str] = pydantic.Field(
        description="Textual description of what are the physician assessments and testing plans."
    )
    payor_code: typing.Optional[str] = pydantic.Field(
        description="Unique identifier representing a specific Health Insurance."
    )
    insurance_id: typing.Optional[str] = pydantic.Field(
        description="Insurance unique number assigned to a patient, usually present on the insurance card."
    )
    responsible_relationship: typing.Optional[ResponsibleRelationship] = pydantic.Field(
        description="Relationship between the patient and the insurance contractor. Values can be (Self, Spouse, Other Relationship)."
    )
    responsible_details: typing.Optional[PersonDetails] = pydantic.Field(
        description="Responsible details when the value of responsible_relationship is not 'Self'."
    )
    diagnosis_codes: typing.Optional[typing.List[str]] = pydantic.Field(
        description="Diagnosis codes for insurance billing."
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
