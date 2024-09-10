# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingLabs(str, enum.Enum):
    QUEST = "quest"
    LABCORP = "labcorp"
    BIOREFERENCE = "bioreference"

    def visit(
        self,
        quest: typing.Callable[[], T_Result],
        labcorp: typing.Callable[[], T_Result],
        bioreference: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingLabs.QUEST:
            return quest()
        if self is ClientFacingLabs.LABCORP:
            return labcorp()
        if self is ClientFacingLabs.BIOREFERENCE:
            return bioreference()
