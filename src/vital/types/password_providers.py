# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PasswordProviders(str, enum.Enum):
    """
    An enumeration.
    """

    WHOOP = "whoop"
    RENPHO = "renpho"
    PELOTON = "peloton"
    ZWIFT = "zwift"
    EIGHT_SLEEP = "eight_sleep"
    BEURER_API = "beurer_api"
    DEXCOM = "dexcom"
    HAMMERHEAD = "hammerhead"
    MY_FITNESS_PAL = "my_fitness_pal"
    KARDIA = "kardia"

    def visit(
        self,
        whoop: typing.Callable[[], T_Result],
        renpho: typing.Callable[[], T_Result],
        peloton: typing.Callable[[], T_Result],
        zwift: typing.Callable[[], T_Result],
        eight_sleep: typing.Callable[[], T_Result],
        beurer_api: typing.Callable[[], T_Result],
        dexcom: typing.Callable[[], T_Result],
        hammerhead: typing.Callable[[], T_Result],
        my_fitness_pal: typing.Callable[[], T_Result],
        kardia: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PasswordProviders.WHOOP:
            return whoop()
        if self is PasswordProviders.RENPHO:
            return renpho()
        if self is PasswordProviders.PELOTON:
            return peloton()
        if self is PasswordProviders.ZWIFT:
            return zwift()
        if self is PasswordProviders.EIGHT_SLEEP:
            return eight_sleep()
        if self is PasswordProviders.BEURER_API:
            return beurer_api()
        if self is PasswordProviders.DEXCOM:
            return dexcom()
        if self is PasswordProviders.HAMMERHEAD:
            return hammerhead()
        if self is PasswordProviders.MY_FITNESS_PAL:
            return my_fitness_pal()
        if self is PasswordProviders.KARDIA:
            return kardia()
