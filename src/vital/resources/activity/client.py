# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.client_activity_response import ClientActivityResponse
from ...types.http_validation_error import HttpValidationError
from ...types.raw_activity import RawActivity

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ActivityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        user_id: str,
        *,
        provider: typing.Optional[str] = None,
        start_date: str,
        end_date: typing.Optional[str] = None,
    ) -> ClientActivityResponse:
        """
        Get Daily Activity for user_id

        Parameters:
            - user_id: str.

            - provider: typing.Optional[str]. Provider oura/strava etc

            - start_date: str. Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00

            - end_date: typing.Optional[str]. Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
        ---
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.get(
            user_id="user-id",
            start_date="start-date",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/summary/activity/{user_id}"),
            params=remove_none_from_dict({"provider": provider, "start_date": start_date, "end_date": end_date}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientActivityResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_raw(
        self,
        user_id: str,
        *,
        provider: typing.Optional[str] = None,
        start_date: str,
        end_date: typing.Optional[str] = None,
    ) -> RawActivity:
        """
        Get Daily Activity for user_id

        Parameters:
            - user_id: str.

            - provider: typing.Optional[str]. Provider oura/strava etc

            - start_date: str. Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00

            - end_date: typing.Optional[str]. Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
        ---
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.get_raw(
            user_id="user-id",
            start_date="start-date",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/summary/activity/{user_id}/raw"),
            params=remove_none_from_dict({"provider": provider, "start_date": start_date, "end_date": end_date}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RawActivity, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncActivityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        user_id: str,
        *,
        provider: typing.Optional[str] = None,
        start_date: str,
        end_date: typing.Optional[str] = None,
    ) -> ClientActivityResponse:
        """
        Get Daily Activity for user_id

        Parameters:
            - user_id: str.

            - provider: typing.Optional[str]. Provider oura/strava etc

            - start_date: str. Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00

            - end_date: typing.Optional[str]. Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.get(
            user_id="user-id",
            start_date="start-date",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/summary/activity/{user_id}"),
            params=remove_none_from_dict({"provider": provider, "start_date": start_date, "end_date": end_date}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientActivityResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_raw(
        self,
        user_id: str,
        *,
        provider: typing.Optional[str] = None,
        start_date: str,
        end_date: typing.Optional[str] = None,
    ) -> RawActivity:
        """
        Get Daily Activity for user_id

        Parameters:
            - user_id: str.

            - provider: typing.Optional[str]. Provider oura/strava etc

            - start_date: str. Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00

            - end_date: typing.Optional[str]. Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.get_raw(
            user_id="user-id",
            start_date="start-date",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/summary/activity/{user_id}/raw"),
            params=remove_none_from_dict({"provider": provider, "start_date": start_date, "end_date": end_date}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RawActivity, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
