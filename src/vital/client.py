# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import VitalEnvironment
from .resources.activity.client import ActivityClient, AsyncActivityClient
from .resources.body.client import AsyncBodyClient, BodyClient
from .resources.devices.client import AsyncDevicesClient, DevicesClient
from .resources.insurance.client import AsyncInsuranceClient, InsuranceClient
from .resources.lab_tests.client import AsyncLabTestsClient, LabTestsClient
from .resources.link.client import AsyncLinkClient, LinkClient
from .resources.meal.client import AsyncMealClient, MealClient
from .resources.profile.client import AsyncProfileClient, ProfileClient
from .resources.providers.client import AsyncProvidersClient, ProvidersClient
from .resources.sleep.client import AsyncSleepClient, SleepClient
from .resources.team.client import AsyncTeamClient, TeamClient
from .resources.testkit.client import AsyncTestkitClient, TestkitClient
from .resources.timeseries.client import AsyncTimeseriesClient, TimeseriesClient
from .resources.user.client import AsyncUserClient, UserClient
from .resources.vitals.client import AsyncVitalsClient, VitalsClient
from .resources.workouts.client import AsyncWorkoutsClient, WorkoutsClient


class Vital:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: VitalEnvironment = VitalEnvironment.PRODUCTION,
        api_key: str,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.Client(timeout=timeout),
        )
        self.link = LinkClient(client_wrapper=self._client_wrapper)
        self.profile = ProfileClient(client_wrapper=self._client_wrapper)
        self.devices = DevicesClient(client_wrapper=self._client_wrapper)
        self.activity = ActivityClient(client_wrapper=self._client_wrapper)
        self.workouts = WorkoutsClient(client_wrapper=self._client_wrapper)
        self.sleep = SleepClient(client_wrapper=self._client_wrapper)
        self.body = BodyClient(client_wrapper=self._client_wrapper)
        self.meal = MealClient(client_wrapper=self._client_wrapper)
        self.timeseries = TimeseriesClient(client_wrapper=self._client_wrapper)
        self.vitals = VitalsClient(client_wrapper=self._client_wrapper)
        self.user = UserClient(client_wrapper=self._client_wrapper)
        self.team = TeamClient(client_wrapper=self._client_wrapper)
        self.providers = ProvidersClient(client_wrapper=self._client_wrapper)
        self.lab_tests = LabTestsClient(client_wrapper=self._client_wrapper)
        self.testkit = TestkitClient(client_wrapper=self._client_wrapper)
        self.insurance = InsuranceClient(client_wrapper=self._client_wrapper)


class AsyncVital:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: VitalEnvironment = VitalEnvironment.PRODUCTION,
        api_key: str,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.AsyncClient(timeout=timeout),
        )
        self.link = AsyncLinkClient(client_wrapper=self._client_wrapper)
        self.profile = AsyncProfileClient(client_wrapper=self._client_wrapper)
        self.devices = AsyncDevicesClient(client_wrapper=self._client_wrapper)
        self.activity = AsyncActivityClient(client_wrapper=self._client_wrapper)
        self.workouts = AsyncWorkoutsClient(client_wrapper=self._client_wrapper)
        self.sleep = AsyncSleepClient(client_wrapper=self._client_wrapper)
        self.body = AsyncBodyClient(client_wrapper=self._client_wrapper)
        self.meal = AsyncMealClient(client_wrapper=self._client_wrapper)
        self.timeseries = AsyncTimeseriesClient(client_wrapper=self._client_wrapper)
        self.vitals = AsyncVitalsClient(client_wrapper=self._client_wrapper)
        self.user = AsyncUserClient(client_wrapper=self._client_wrapper)
        self.team = AsyncTeamClient(client_wrapper=self._client_wrapper)
        self.providers = AsyncProvidersClient(client_wrapper=self._client_wrapper)
        self.lab_tests = AsyncLabTestsClient(client_wrapper=self._client_wrapper)
        self.testkit = AsyncTestkitClient(client_wrapper=self._client_wrapper)
        self.insurance = AsyncInsuranceClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: VitalEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
