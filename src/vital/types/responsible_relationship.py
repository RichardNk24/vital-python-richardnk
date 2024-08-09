# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResponsibleRelationship(str, enum.Enum):
    SELF = "Self"
    SPOUSE = "Spouse"
    OTHER = "Other"

    def visit(
        self,
        self_: typing.Callable[[], T_Result],
        spouse: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResponsibleRelationship.SELF:
            return self_()
        if self is ResponsibleRelationship.SPOUSE:
            return spouse()
        if self is ResponsibleRelationship.OTHER:
            return other()
