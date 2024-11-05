# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SleepType(str, enum.Enum):
    LONG_SLEEP = "long_sleep"
    SHORT_SLEEP = "short_sleep"
    ACKNOWLEDGED_NAP = "acknowledged_nap"
    UNKNOWN = "unknown"

    def visit(
        self,
        long_sleep: typing.Callable[[], T_Result],
        short_sleep: typing.Callable[[], T_Result],
        acknowledged_nap: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SleepType.LONG_SLEEP:
            return long_sleep()
        if self is SleepType.SHORT_SLEEP:
            return short_sleep()
        if self is SleepType.ACKNOWLEDGED_NAP:
            return acknowledged_nap()
        if self is SleepType.UNKNOWN:
            return unknown()
