# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Providers(str, enum.Enum):
    OURA = "oura"
    FITBIT = "fitbit"
    GARMIN = "garmin"
    WHOOP = "whoop"
    STRAVA = "strava"
    RENPHO = "renpho"
    PELOTON = "peloton"
    WAHOO = "wahoo"
    ZWIFT = "zwift"
    FREESTYLE_LIBRE = "freestyle_libre"
    ABBOTT_LIBREVIEW = "abbott_libreview"
    FREESTYLE_LIBRE_BLE = "freestyle_libre_ble"
    EIGHT_SLEEP = "eight_sleep"
    WITHINGS = "withings"
    APPLE_HEALTH_KIT = "apple_health_kit"
    MANUAL = "manual"
    IHEALTH = "ihealth"
    GOOGLE_FIT = "google_fit"
    BEURER_API = "beurer_api"
    BEURER_BLE = "beurer_ble"
    OMRON = "omron"
    OMRON_BLE = "omron_ble"
    ONETOUCH_BLE = "onetouch_ble"
    ACCUCHEK_BLE = "accuchek_ble"
    CONTOUR_BLE = "contour_ble"
    DEXCOM = "dexcom"
    DEXCOM_V_3 = "dexcom_v3"
    HAMMERHEAD = "hammerhead"
    MY_FITNESS_PAL = "my_fitness_pal"
    HEALTH_CONNECT = "health_connect"
    POLAR = "polar"
    CRONOMETER = "cronometer"
    KARDIA = "kardia"
    WHOOP_V_2 = "whoop_v2"
    ULTRAHUMAN = "ultrahuman"
    MY_FITNESS_PAL_V_2 = "my_fitness_pal_v2"

    def visit(
        self,
        oura: typing.Callable[[], T_Result],
        fitbit: typing.Callable[[], T_Result],
        garmin: typing.Callable[[], T_Result],
        whoop: typing.Callable[[], T_Result],
        strava: typing.Callable[[], T_Result],
        renpho: typing.Callable[[], T_Result],
        peloton: typing.Callable[[], T_Result],
        wahoo: typing.Callable[[], T_Result],
        zwift: typing.Callable[[], T_Result],
        freestyle_libre: typing.Callable[[], T_Result],
        abbott_libreview: typing.Callable[[], T_Result],
        freestyle_libre_ble: typing.Callable[[], T_Result],
        eight_sleep: typing.Callable[[], T_Result],
        withings: typing.Callable[[], T_Result],
        apple_health_kit: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        ihealth: typing.Callable[[], T_Result],
        google_fit: typing.Callable[[], T_Result],
        beurer_api: typing.Callable[[], T_Result],
        beurer_ble: typing.Callable[[], T_Result],
        omron: typing.Callable[[], T_Result],
        omron_ble: typing.Callable[[], T_Result],
        onetouch_ble: typing.Callable[[], T_Result],
        accuchek_ble: typing.Callable[[], T_Result],
        contour_ble: typing.Callable[[], T_Result],
        dexcom: typing.Callable[[], T_Result],
        dexcom_v_3: typing.Callable[[], T_Result],
        hammerhead: typing.Callable[[], T_Result],
        my_fitness_pal: typing.Callable[[], T_Result],
        health_connect: typing.Callable[[], T_Result],
        polar: typing.Callable[[], T_Result],
        cronometer: typing.Callable[[], T_Result],
        kardia: typing.Callable[[], T_Result],
        whoop_v_2: typing.Callable[[], T_Result],
        ultrahuman: typing.Callable[[], T_Result],
        my_fitness_pal_v_2: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Providers.OURA:
            return oura()
        if self is Providers.FITBIT:
            return fitbit()
        if self is Providers.GARMIN:
            return garmin()
        if self is Providers.WHOOP:
            return whoop()
        if self is Providers.STRAVA:
            return strava()
        if self is Providers.RENPHO:
            return renpho()
        if self is Providers.PELOTON:
            return peloton()
        if self is Providers.WAHOO:
            return wahoo()
        if self is Providers.ZWIFT:
            return zwift()
        if self is Providers.FREESTYLE_LIBRE:
            return freestyle_libre()
        if self is Providers.ABBOTT_LIBREVIEW:
            return abbott_libreview()
        if self is Providers.FREESTYLE_LIBRE_BLE:
            return freestyle_libre_ble()
        if self is Providers.EIGHT_SLEEP:
            return eight_sleep()
        if self is Providers.WITHINGS:
            return withings()
        if self is Providers.APPLE_HEALTH_KIT:
            return apple_health_kit()
        if self is Providers.MANUAL:
            return manual()
        if self is Providers.IHEALTH:
            return ihealth()
        if self is Providers.GOOGLE_FIT:
            return google_fit()
        if self is Providers.BEURER_API:
            return beurer_api()
        if self is Providers.BEURER_BLE:
            return beurer_ble()
        if self is Providers.OMRON:
            return omron()
        if self is Providers.OMRON_BLE:
            return omron_ble()
        if self is Providers.ONETOUCH_BLE:
            return onetouch_ble()
        if self is Providers.ACCUCHEK_BLE:
            return accuchek_ble()
        if self is Providers.CONTOUR_BLE:
            return contour_ble()
        if self is Providers.DEXCOM:
            return dexcom()
        if self is Providers.DEXCOM_V_3:
            return dexcom_v_3()
        if self is Providers.HAMMERHEAD:
            return hammerhead()
        if self is Providers.MY_FITNESS_PAL:
            return my_fitness_pal()
        if self is Providers.HEALTH_CONNECT:
            return health_connect()
        if self is Providers.POLAR:
            return polar()
        if self is Providers.CRONOMETER:
            return cronometer()
        if self is Providers.KARDIA:
            return kardia()
        if self is Providers.WHOOP_V_2:
            return whoop_v_2()
        if self is Providers.ULTRAHUMAN:
            return ultrahuman()
        if self is Providers.MY_FITNESS_PAL_V_2:
            return my_fitness_pal_v_2()
