# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FailureType(str, enum.Enum):
    QUANTITY_NOT_SUFFICIENT_FAILURE = "quantity_not_sufficient_failure"
    COLLECTION_PROCESS_FAILURE = "collection_process_failure"
    DROP_OFF_FAILURE = "drop_off_failure"
    INTERNAL_LAB_FAILURE = "internal_lab_failure"
    ORDER_ENTRY_FAILURE = "order_entry_failure"
    NON_FAILURE = "non_failure"
    UNKNOWN_FAILURE = "unknown_failure"
    PATIENT_CONDITION_FAILURE = "patient_condition_failure"
    MISSING_RESULT_CALC_FAILURE = "missing_result_calc_failure"
    MISSING_DEMO_AOE_CALC_FAILURE = "missing_demo_aoe_calc_failure"

    def visit(
        self,
        quantity_not_sufficient_failure: typing.Callable[[], T_Result],
        collection_process_failure: typing.Callable[[], T_Result],
        drop_off_failure: typing.Callable[[], T_Result],
        internal_lab_failure: typing.Callable[[], T_Result],
        order_entry_failure: typing.Callable[[], T_Result],
        non_failure: typing.Callable[[], T_Result],
        unknown_failure: typing.Callable[[], T_Result],
        patient_condition_failure: typing.Callable[[], T_Result],
        missing_result_calc_failure: typing.Callable[[], T_Result],
        missing_demo_aoe_calc_failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FailureType.QUANTITY_NOT_SUFFICIENT_FAILURE:
            return quantity_not_sufficient_failure()
        if self is FailureType.COLLECTION_PROCESS_FAILURE:
            return collection_process_failure()
        if self is FailureType.DROP_OFF_FAILURE:
            return drop_off_failure()
        if self is FailureType.INTERNAL_LAB_FAILURE:
            return internal_lab_failure()
        if self is FailureType.ORDER_ENTRY_FAILURE:
            return order_entry_failure()
        if self is FailureType.NON_FAILURE:
            return non_failure()
        if self is FailureType.UNKNOWN_FAILURE:
            return unknown_failure()
        if self is FailureType.PATIENT_CONDITION_FAILURE:
            return patient_condition_failure()
        if self is FailureType.MISSING_RESULT_CALC_FAILURE:
            return missing_result_calc_failure()
        if self is FailureType.MISSING_DEMO_AOE_CALC_FAILURE:
            return missing_demo_aoe_calc_failure()
