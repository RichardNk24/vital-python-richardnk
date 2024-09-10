# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.client_facing_payor_search_response import ClientFacingPayorSearchResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.client_facing_diagnosis_information import ClientFacingDiagnosisInformation
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InsuranceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_payor_info(
        self, *, insurance_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ClientFacingPayorSearchResponse]:
        """
        Parameters
        ----------
        insurance_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClientFacingPayorSearchResponse]
            Successful Response

        Examples
        --------
        from vital import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.insurance.search_payor_info(
            insurance_name="insurance_name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/insurance/search/payor",
            method="POST",
            json={
                "insurance_name": insurance_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ClientFacingPayorSearchResponse],
                    parse_obj_as(
                        type_=typing.List[ClientFacingPayorSearchResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def search_diagnosis(
        self, *, diagnosis_query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ClientFacingDiagnosisInformation]:
        """
        Parameters
        ----------
        diagnosis_query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClientFacingDiagnosisInformation]
            Successful Response

        Examples
        --------
        from vital import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.insurance.search_diagnosis(
            diagnosis_query="diagnosis_query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/insurance/search/diagnosis",
            method="GET",
            params={
                "diagnosis_query": diagnosis_query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ClientFacingDiagnosisInformation],
                    parse_obj_as(
                        type_=typing.List[ClientFacingDiagnosisInformation],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInsuranceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_payor_info(
        self, *, insurance_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ClientFacingPayorSearchResponse]:
        """
        Parameters
        ----------
        insurance_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClientFacingPayorSearchResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from vital import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insurance.search_payor_info(
                insurance_name="insurance_name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/insurance/search/payor",
            method="POST",
            json={
                "insurance_name": insurance_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ClientFacingPayorSearchResponse],
                    parse_obj_as(
                        type_=typing.List[ClientFacingPayorSearchResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def search_diagnosis(
        self, *, diagnosis_query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ClientFacingDiagnosisInformation]:
        """
        Parameters
        ----------
        diagnosis_query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClientFacingDiagnosisInformation]
            Successful Response

        Examples
        --------
        import asyncio

        from vital import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insurance.search_diagnosis(
                diagnosis_query="diagnosis_query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/insurance/search/diagnosis",
            method="GET",
            params={
                "diagnosis_query": diagnosis_query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ClientFacingDiagnosisInformation],
                    parse_obj_as(
                        type_=typing.List[ClientFacingDiagnosisInformation],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
