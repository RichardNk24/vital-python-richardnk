# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .client_facing_source import ClientFacingSource
from .client_facing_heart_rate import ClientFacingHeartRate
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientFacingActivity(UniversalBaseModel):
    user_id: str = pydantic.Field()
    """
    User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api.
    """

    id: str
    date: str = pydantic.Field()
    """
    Date of the specified record, formatted as ISO8601 datetime string in UTC 00:00. Deprecated in favour of calendar_date.
    """

    calendar_date: str = pydantic.Field()
    """
    Date of the summary in the YYYY-mm-dd format.
    """

    calories_total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total energy consumption during the day including Basal Metabolic Rate in kilocalories::kilocalories
    """

    calories_active: typing.Optional[float] = pydantic.Field(default=None)
    """
    Energy consumption caused by the physical activity of the day in kilocalories::kilocalories
    """

    steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of steps registered during the day::steps
    """

    daily_movement: typing.Optional[float] = pydantic.Field(default=None)
    """
    Deprecated. Daily physical activity as equal meters i.e. amount of walking needed to get the same amount of activity::meters
    """

    distance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Distance traveled during activities throughout the day::meters
    """

    low: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of minutes during the day with low intensity activity (e.g. household work)::minutes
    """

    medium: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of minutes during the day with medium intensity activity (e.g. walking)::minutes
    """

    high: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of minutes during the day with high intensity activity (e.g. running)::minutes
    """

    source: ClientFacingSource = pydantic.Field()
    """
    Source the data has come from.
    """

    floors_climbed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of floors climbed by the user::count
    """

    time_zone: typing.Optional[str] = pydantic.Field(default=None)
    """
    [DEPRECATED] The time zone full identifier for the data. Example: 'Europe/London'.
    """

    timezone_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timezone offset from UTC as seconds. For example, EEST (Eastern European Summer Time, +3h) is 10800. PST (Pacific Standard Time, -8h) is -28800::seconds
    """

    heart_rate: typing.Optional[ClientFacingHeartRate] = pydantic.Field(default=None)
    """
    Heart rate daily summary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
