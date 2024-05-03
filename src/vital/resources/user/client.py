# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.client_facing_provider_with_status import ClientFacingProviderWithStatus
from ...types.client_facing_user import ClientFacingUser
from ...types.client_facing_user_key import ClientFacingUserKey
from ...types.http_validation_error import HttpValidationError
from ...types.metrics_result import MetricsResult
from ...types.paginated_users_response import PaginatedUsersResponse
from ...types.providers import Providers
from ...types.user_refresh_success_response import UserRefreshSuccessResponse
from ...types.user_sign_in_token_response import UserSignInTokenResponse
from ...types.user_success_response import UserSuccessResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all(
        self, *, offset: typing.Optional[int] = None, limit: typing.Optional[int] = None
    ) -> PaginatedUsersResponse:
        """
        GET All users for team.

        Parameters:
            - offset: typing.Optional[int].

            - limit: typing.Optional[int].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user"),
            params=remove_none_from_dict({"offset": offset, "limit": limit}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedUsersResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        client_user_id: str,
        fallback_time_zone: typing.Optional[str] = OMIT,
        fallback_birth_date: typing.Optional[str] = OMIT,
        ingestion_start: typing.Optional[str] = OMIT,
        ingestion_end: typing.Optional[str] = OMIT,
    ) -> ClientFacingUserKey:
        """
        POST Create a Vital user given a client_user_id and returns the user_id.

        Parameters:
            - client_user_id: str. A unique ID representing the end user. Typically this will be a user ID from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id.

            - fallback_time_zone: typing.Optional[str].
                                                            Fallback time zone of the user, in the form of a valid IANA tzdatabase identifier (e.g., `Europe/London` or `America/Los_Angeles`).
                                                            Used when pulling data from sources that are completely time zone agnostic (e.g., all time is relative to UTC clock, without any time zone attributions on data points).

            - fallback_birth_date: typing.Optional[str]. Fallback date of birth of the user, in YYYY-mm-dd format. Used for calculating max heartrate for providers that don not provide users' age.

            - ingestion_start: typing.Optional[str]. Starting bound for user data ingestion. Data older than this date will not be ingested.

            - ingestion_end: typing.Optional[str]. Ending bound for user data ingestion. Data newer than this date will not be ingested and the connection deregistered.
        """
        _request: typing.Dict[str, typing.Any] = {"client_user_id": client_user_id}
        if fallback_time_zone is not OMIT:
            _request["fallback_time_zone"] = fallback_time_zone
        if fallback_birth_date is not OMIT:
            _request["fallback_birth_date"] = fallback_birth_date
        if ingestion_start is not OMIT:
            _request["ingestion_start"] = ingestion_start
        if ingestion_end is not OMIT:
            _request["ingestion_end"] = ingestion_end
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingUserKey, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_team_metrics(self) -> MetricsResult:
        """
        GET metrics for team.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user/metrics"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetricsResult, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_user_sign_in_token(self, user_id: str) -> UserSignInTokenResponse:
        """
        Parameters:
            - user_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}/sign_in_token"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSignInTokenResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_connected_providers(self, user_id: str) -> typing.Dict[str, typing.List[ClientFacingProviderWithStatus]]:
        """
        GET Users connected providers

        Parameters:
            - user_id: str.
        ---
        from vital.client import Vital

        client = Vital(
            vital_link_token="YOUR_VITAL_LINK_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.user.get_connected_providers(
            user_id="user-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/providers/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.List[ClientFacingProviderWithStatus]], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, user_id: str) -> ClientFacingUser:
        """
        GET User details given the user_id.

        Parameters:
            - user_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingUser, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, user_id: str) -> UserSuccessResponse:
        """
        Parameters:
            - user_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch(
        self,
        user_id: str,
        *,
        fallback_time_zone: typing.Optional[str] = OMIT,
        fallback_birth_date: typing.Optional[str] = OMIT,
        ingestion_start: typing.Optional[str] = OMIT,
        ingestion_end: typing.Optional[str] = OMIT,
    ) -> None:
        """
        Parameters:
            - user_id: str.

            - fallback_time_zone: typing.Optional[str].
                                                            Fallback time zone of the user, in the form of a valid IANA tzdatabase identifier (e.g., `Europe/London` or `America/Los_Angeles`).
                                                            Used when pulling data from sources that are completely time zone agnostic (e.g., all time is relative to UTC clock, without any time zone attributions on data points).

            - fallback_birth_date: typing.Optional[str]. Fallback date of birth of the user, in YYYY-mm-dd format. Used for calculating max heartrate for providers that don not provide users' age.

            - ingestion_start: typing.Optional[str]. Starting bound for user data ingestion. Data older than this date will not be ingested.

            - ingestion_end: typing.Optional[str]. Ending bound for user data ingestion. Data newer than this date will not be ingested and the connection deregistered.
        ---
        from vital.client import Vital

        client = Vital(
            vital_link_token="YOUR_VITAL_LINK_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.user.patch(
            user_id="user-id",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if fallback_time_zone is not OMIT:
            _request["fallback_time_zone"] = fallback_time_zone
        if fallback_birth_date is not OMIT:
            _request["fallback_birth_date"] = fallback_birth_date
        if ingestion_start is not OMIT:
            _request["ingestion_start"] = ingestion_start
        if ingestion_end is not OMIT:
            _request["ingestion_end"] = ingestion_end
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_by_client_user_id(self, client_user_id: str) -> ClientFacingUser:
        """
        GET user_id from client_user_id.

        Parameters:
            - client_user_id: str. A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/resolve/{client_user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingUser, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def deregister_provider(self, user_id: str, provider: Providers) -> UserSuccessResponse:
        """
        Parameters:
            - user_id: str.

            - provider: Providers. Provider slug. e.g., `oura`, `fitbit`, `garmin`.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}/{provider}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def undo_delete(
        self, *, user_id: typing.Optional[str] = None, client_user_id: typing.Optional[str] = None
    ) -> UserSuccessResponse:
        """
        Parameters:
            - user_id: typing.Optional[str]. User ID to undo deletion. Mutually exclusive with `client_user_id`.

            - client_user_id: typing.Optional[str]. Client User ID to undo deletion. Mutually exclusive with `user_id`.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user/undo_delete"),
            params=remove_none_from_dict({"user_id": user_id, "client_user_id": client_user_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def refresh(self, user_id: str, *, timeout: typing.Optional[float] = None) -> UserRefreshSuccessResponse:
        """
        Trigger a manual refresh for a specific user

        Parameters:
            - user_id: str.

            - timeout: typing.Optional[float].
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/refresh/{user_id}"),
            params=remove_none_from_dict({"timeout": timeout}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserRefreshSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all(
        self, *, offset: typing.Optional[int] = None, limit: typing.Optional[int] = None
    ) -> PaginatedUsersResponse:
        """
        GET All users for team.

        Parameters:
            - offset: typing.Optional[int].

            - limit: typing.Optional[int].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user"),
            params=remove_none_from_dict({"offset": offset, "limit": limit}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedUsersResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        client_user_id: str,
        fallback_time_zone: typing.Optional[str] = OMIT,
        fallback_birth_date: typing.Optional[str] = OMIT,
        ingestion_start: typing.Optional[str] = OMIT,
        ingestion_end: typing.Optional[str] = OMIT,
    ) -> ClientFacingUserKey:
        """
        POST Create a Vital user given a client_user_id and returns the user_id.

        Parameters:
            - client_user_id: str. A unique ID representing the end user. Typically this will be a user ID from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id.

            - fallback_time_zone: typing.Optional[str].
                                                            Fallback time zone of the user, in the form of a valid IANA tzdatabase identifier (e.g., `Europe/London` or `America/Los_Angeles`).
                                                            Used when pulling data from sources that are completely time zone agnostic (e.g., all time is relative to UTC clock, without any time zone attributions on data points).

            - fallback_birth_date: typing.Optional[str]. Fallback date of birth of the user, in YYYY-mm-dd format. Used for calculating max heartrate for providers that don not provide users' age.

            - ingestion_start: typing.Optional[str]. Starting bound for user data ingestion. Data older than this date will not be ingested.

            - ingestion_end: typing.Optional[str]. Ending bound for user data ingestion. Data newer than this date will not be ingested and the connection deregistered.
        """
        _request: typing.Dict[str, typing.Any] = {"client_user_id": client_user_id}
        if fallback_time_zone is not OMIT:
            _request["fallback_time_zone"] = fallback_time_zone
        if fallback_birth_date is not OMIT:
            _request["fallback_birth_date"] = fallback_birth_date
        if ingestion_start is not OMIT:
            _request["ingestion_start"] = ingestion_start
        if ingestion_end is not OMIT:
            _request["ingestion_end"] = ingestion_end
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingUserKey, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_team_metrics(self) -> MetricsResult:
        """
        GET metrics for team.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user/metrics"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetricsResult, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_user_sign_in_token(self, user_id: str) -> UserSignInTokenResponse:
        """
        Parameters:
            - user_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}/sign_in_token"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSignInTokenResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_connected_providers(
        self, user_id: str
    ) -> typing.Dict[str, typing.List[ClientFacingProviderWithStatus]]:
        """
        GET Users connected providers

        Parameters:
            - user_id: str.
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            vital_link_token="YOUR_VITAL_LINK_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.user.get_connected_providers(
            user_id="user-id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/providers/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.List[ClientFacingProviderWithStatus]], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, user_id: str) -> ClientFacingUser:
        """
        GET User details given the user_id.

        Parameters:
            - user_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingUser, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, user_id: str) -> UserSuccessResponse:
        """
        Parameters:
            - user_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch(
        self,
        user_id: str,
        *,
        fallback_time_zone: typing.Optional[str] = OMIT,
        fallback_birth_date: typing.Optional[str] = OMIT,
        ingestion_start: typing.Optional[str] = OMIT,
        ingestion_end: typing.Optional[str] = OMIT,
    ) -> None:
        """
        Parameters:
            - user_id: str.

            - fallback_time_zone: typing.Optional[str].
                                                            Fallback time zone of the user, in the form of a valid IANA tzdatabase identifier (e.g., `Europe/London` or `America/Los_Angeles`).
                                                            Used when pulling data from sources that are completely time zone agnostic (e.g., all time is relative to UTC clock, without any time zone attributions on data points).

            - fallback_birth_date: typing.Optional[str]. Fallback date of birth of the user, in YYYY-mm-dd format. Used for calculating max heartrate for providers that don not provide users' age.

            - ingestion_start: typing.Optional[str]. Starting bound for user data ingestion. Data older than this date will not be ingested.

            - ingestion_end: typing.Optional[str]. Ending bound for user data ingestion. Data newer than this date will not be ingested and the connection deregistered.
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            vital_link_token="YOUR_VITAL_LINK_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.user.patch(
            user_id="user-id",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if fallback_time_zone is not OMIT:
            _request["fallback_time_zone"] = fallback_time_zone
        if fallback_birth_date is not OMIT:
            _request["fallback_birth_date"] = fallback_birth_date
        if ingestion_start is not OMIT:
            _request["ingestion_start"] = ingestion_start
        if ingestion_end is not OMIT:
            _request["ingestion_end"] = ingestion_end
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_by_client_user_id(self, client_user_id: str) -> ClientFacingUser:
        """
        GET user_id from client_user_id.

        Parameters:
            - client_user_id: str. A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/resolve/{client_user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingUser, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def deregister_provider(self, user_id: str, provider: Providers) -> UserSuccessResponse:
        """
        Parameters:
            - user_id: str.

            - provider: Providers. Provider slug. e.g., `oura`, `fitbit`, `garmin`.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/{user_id}/{provider}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def undo_delete(
        self, *, user_id: typing.Optional[str] = None, client_user_id: typing.Optional[str] = None
    ) -> UserSuccessResponse:
        """
        Parameters:
            - user_id: typing.Optional[str]. User ID to undo deletion. Mutually exclusive with `client_user_id`.

            - client_user_id: typing.Optional[str]. Client User ID to undo deletion. Mutually exclusive with `user_id`.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/user/undo_delete"),
            params=remove_none_from_dict({"user_id": user_id, "client_user_id": client_user_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def refresh(self, user_id: str, *, timeout: typing.Optional[float] = None) -> UserRefreshSuccessResponse:
        """
        Trigger a manual refresh for a specific user

        Parameters:
            - user_id: str.

            - timeout: typing.Optional[float].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/user/refresh/{user_id}"),
            params=remove_none_from_dict({"timeout": timeout}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserRefreshSuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
