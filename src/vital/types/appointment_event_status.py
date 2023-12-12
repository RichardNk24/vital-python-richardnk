# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AppointmentEventStatus(str, enum.Enum):
    """
    An enumeration.
    """

    PENDING = "pending"
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    IN_PROGRESS = "in_progress"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppointmentEventStatus.PENDING:
            return pending()
        if self is AppointmentEventStatus.SCHEDULED:
            return scheduled()
        if self is AppointmentEventStatus.COMPLETED:
            return completed()
        if self is AppointmentEventStatus.CANCELLED:
            return cancelled()
        if self is AppointmentEventStatus.IN_PROGRESS:
            return in_progress()
