# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(self, *, api_key: str, base_url: str):
        self.api_key = api_key
        self._base_url = base_url

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "vital",
            "X-Fern-SDK-Version": "2.1.30",
        }
        headers["x-vital-api-key"] = self.api_key
        return headers

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, api_key: str, base_url: str, httpx_client: httpx.Client):
        super().__init__(api_key=api_key, base_url=base_url)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, api_key: str, base_url: str, httpx_client: httpx.AsyncClient):
        super().__init__(api_key=api_key, base_url=base_url)
        self.httpx_client = httpx_client
