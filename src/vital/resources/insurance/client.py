# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.client_facing_diagnosis_information import ClientFacingDiagnosisInformation
from ...types.client_facing_payor_search_response import ClientFacingPayorSearchResponse
from ...types.http_validation_error import HttpValidationError

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InsuranceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_payor_info(
        self, *, insurance_name: str, insurance_state: typing.Optional[str] = OMIT
    ) -> typing.List[ClientFacingPayorSearchResponse]:
        """
        Parameters:
            - insurance_name: str.

            - insurance_state: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"insurance_name": insurance_name}
        if insurance_state is not OMIT:
            _request["insurance_state"] = insurance_state
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/insurance/search/payor"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingPayorSearchResponse], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def search_diagnosis(self, *, diagnosis_query: str) -> typing.List[ClientFacingDiagnosisInformation]:
        """
        Parameters:
            - diagnosis_query: str.
        ---
        from vital.client import Vital

        client = Vital(
            vital_link_token="YOUR_VITAL_LINK_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.insurance.search_diagnosis(
            diagnosis_query="diagnosis-query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/insurance/search/diagnosis"),
            params=remove_none_from_dict({"diagnosis_query": diagnosis_query}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingDiagnosisInformation], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInsuranceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_payor_info(
        self, *, insurance_name: str, insurance_state: typing.Optional[str] = OMIT
    ) -> typing.List[ClientFacingPayorSearchResponse]:
        """
        Parameters:
            - insurance_name: str.

            - insurance_state: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"insurance_name": insurance_name}
        if insurance_state is not OMIT:
            _request["insurance_state"] = insurance_state
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/insurance/search/payor"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingPayorSearchResponse], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def search_diagnosis(self, *, diagnosis_query: str) -> typing.List[ClientFacingDiagnosisInformation]:
        """
        Parameters:
            - diagnosis_query: str.
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            vital_link_token="YOUR_VITAL_LINK_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.insurance.search_diagnosis(
            diagnosis_query="diagnosis-query",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v3/insurance/search/diagnosis"),
            params=remove_none_from_dict({"diagnosis_query": diagnosis_query}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingDiagnosisInformation], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
