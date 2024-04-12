# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderStatus(str, enum.Enum):
    """
    An enumeration.
    """

    RECEIVED_WALK_IN_TEST_ORDERED = "received.walk_in_test.ordered"
    RECEIVED_WALK_IN_TEST_REQUISITION_CREATED = "received.walk_in_test.requisition_created"
    COMPLETED_WALK_IN_TEST_COMPLETED = "completed.walk_in_test.completed"
    SAMPLE_WITH_LAB_WALK_IN_TEST_PARTIAL_RESULTS = "sample_with_lab.walk_in_test.partial_results"
    FAILED_WALK_IN_TEST_SAMPLE_ERROR = "failed.walk_in_test.sample_error"
    CANCELLED_WALK_IN_TEST_CANCELLED = "cancelled.walk_in_test.cancelled"
    RECEIVED_AT_HOME_PHLEBOTOMY_ORDERED = "received.at_home_phlebotomy.ordered"
    RECEIVED_AT_HOME_PHLEBOTOMY_REQUISITION_CREATED = "received.at_home_phlebotomy.requisition_created"
    COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_APPOINTMENT_PENDING = (
        "collecting_sample.at_home_phlebotomy.appointment_pending"
    )
    COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_APPOINTMENT_SCHEDULED = (
        "collecting_sample.at_home_phlebotomy.appointment_scheduled"
    )
    COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_DRAW_COMPLETED = "collecting_sample.at_home_phlebotomy.draw_completed"
    COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_APPOINTMENT_CANCELLED = (
        "collecting_sample.at_home_phlebotomy.appointment_cancelled"
    )
    COMPLETED_AT_HOME_PHLEBOTOMY_COMPLETED = "completed.at_home_phlebotomy.completed"
    SAMPLE_WITH_LAB_AT_HOME_PHLEBOTOMY_PARTIAL_RESULTS = "sample_with_lab.at_home_phlebotomy.partial_results"
    CANCELLED_AT_HOME_PHLEBOTOMY_CANCELLED = "cancelled.at_home_phlebotomy.cancelled"
    FAILED_AT_HOME_PHLEBOTOMY_SAMPLE_ERROR = "failed.at_home_phlebotomy.sample_error"
    RECEIVED_TESTKIT_ORDERED = "received.testkit.ordered"
    RECEIVED_TESTKIT_AWAITING_REGISTRATION = "received.testkit.awaiting_registration"
    RECEIVED_TESTKIT_REQUISITION_CREATED = "received.testkit.requisition_created"
    RECEIVED_TESTKIT_REGISTERED = "received.testkit.registered"
    COLLECTING_SAMPLE_TESTKIT_TRANSIT_CUSTOMER = "collecting_sample.testkit.transit_customer"
    COLLECTING_SAMPLE_TESTKIT_OUT_FOR_DELIVERY = "collecting_sample.testkit.out_for_delivery"
    COLLECTING_SAMPLE_TESTKIT_WITH_CUSTOMER = "collecting_sample.testkit.with_customer"
    COLLECTING_SAMPLE_TESTKIT_TRANSIT_LAB = "collecting_sample.testkit.transit_lab"
    SAMPLE_WITH_LAB_TESTKIT_DELIVERED_TO_LAB = "sample_with_lab.testkit.delivered_to_lab"
    COMPLETED_TESTKIT_COMPLETED = "completed.testkit.completed"
    FAILED_TESTKIT_FAILURE_TO_DELIVER_TO_CUSTOMER = "failed.testkit.failure_to_deliver_to_customer"
    FAILED_TESTKIT_FAILURE_TO_DELIVER_TO_LAB = "failed.testkit.failure_to_deliver_to_lab"
    FAILED_TESTKIT_SAMPLE_ERROR = "failed.testkit.sample_error"
    FAILED_TESTKIT_LOST = "failed.testkit.lost"
    CANCELLED_TESTKIT_CANCELLED = "cancelled.testkit.cancelled"
    CANCELLED_TESTKIT_DO_NOT_PROCESS = "cancelled.testkit.do_not_process"

    def visit(
        self,
        received_walk_in_test_ordered: typing.Callable[[], T_Result],
        received_walk_in_test_requisition_created: typing.Callable[[], T_Result],
        completed_walk_in_test_completed: typing.Callable[[], T_Result],
        sample_with_lab_walk_in_test_partial_results: typing.Callable[[], T_Result],
        failed_walk_in_test_sample_error: typing.Callable[[], T_Result],
        cancelled_walk_in_test_cancelled: typing.Callable[[], T_Result],
        received_at_home_phlebotomy_ordered: typing.Callable[[], T_Result],
        received_at_home_phlebotomy_requisition_created: typing.Callable[[], T_Result],
        collecting_sample_at_home_phlebotomy_appointment_pending: typing.Callable[[], T_Result],
        collecting_sample_at_home_phlebotomy_appointment_scheduled: typing.Callable[[], T_Result],
        collecting_sample_at_home_phlebotomy_draw_completed: typing.Callable[[], T_Result],
        collecting_sample_at_home_phlebotomy_appointment_cancelled: typing.Callable[[], T_Result],
        completed_at_home_phlebotomy_completed: typing.Callable[[], T_Result],
        sample_with_lab_at_home_phlebotomy_partial_results: typing.Callable[[], T_Result],
        cancelled_at_home_phlebotomy_cancelled: typing.Callable[[], T_Result],
        failed_at_home_phlebotomy_sample_error: typing.Callable[[], T_Result],
        received_testkit_ordered: typing.Callable[[], T_Result],
        received_testkit_awaiting_registration: typing.Callable[[], T_Result],
        received_testkit_requisition_created: typing.Callable[[], T_Result],
        received_testkit_registered: typing.Callable[[], T_Result],
        collecting_sample_testkit_transit_customer: typing.Callable[[], T_Result],
        collecting_sample_testkit_out_for_delivery: typing.Callable[[], T_Result],
        collecting_sample_testkit_with_customer: typing.Callable[[], T_Result],
        collecting_sample_testkit_transit_lab: typing.Callable[[], T_Result],
        sample_with_lab_testkit_delivered_to_lab: typing.Callable[[], T_Result],
        completed_testkit_completed: typing.Callable[[], T_Result],
        failed_testkit_failure_to_deliver_to_customer: typing.Callable[[], T_Result],
        failed_testkit_failure_to_deliver_to_lab: typing.Callable[[], T_Result],
        failed_testkit_sample_error: typing.Callable[[], T_Result],
        failed_testkit_lost: typing.Callable[[], T_Result],
        cancelled_testkit_cancelled: typing.Callable[[], T_Result],
        cancelled_testkit_do_not_process: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderStatus.RECEIVED_WALK_IN_TEST_ORDERED:
            return received_walk_in_test_ordered()
        if self is OrderStatus.RECEIVED_WALK_IN_TEST_REQUISITION_CREATED:
            return received_walk_in_test_requisition_created()
        if self is OrderStatus.COMPLETED_WALK_IN_TEST_COMPLETED:
            return completed_walk_in_test_completed()
        if self is OrderStatus.SAMPLE_WITH_LAB_WALK_IN_TEST_PARTIAL_RESULTS:
            return sample_with_lab_walk_in_test_partial_results()
        if self is OrderStatus.FAILED_WALK_IN_TEST_SAMPLE_ERROR:
            return failed_walk_in_test_sample_error()
        if self is OrderStatus.CANCELLED_WALK_IN_TEST_CANCELLED:
            return cancelled_walk_in_test_cancelled()
        if self is OrderStatus.RECEIVED_AT_HOME_PHLEBOTOMY_ORDERED:
            return received_at_home_phlebotomy_ordered()
        if self is OrderStatus.RECEIVED_AT_HOME_PHLEBOTOMY_REQUISITION_CREATED:
            return received_at_home_phlebotomy_requisition_created()
        if self is OrderStatus.COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_APPOINTMENT_PENDING:
            return collecting_sample_at_home_phlebotomy_appointment_pending()
        if self is OrderStatus.COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_APPOINTMENT_SCHEDULED:
            return collecting_sample_at_home_phlebotomy_appointment_scheduled()
        if self is OrderStatus.COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_DRAW_COMPLETED:
            return collecting_sample_at_home_phlebotomy_draw_completed()
        if self is OrderStatus.COLLECTING_SAMPLE_AT_HOME_PHLEBOTOMY_APPOINTMENT_CANCELLED:
            return collecting_sample_at_home_phlebotomy_appointment_cancelled()
        if self is OrderStatus.COMPLETED_AT_HOME_PHLEBOTOMY_COMPLETED:
            return completed_at_home_phlebotomy_completed()
        if self is OrderStatus.SAMPLE_WITH_LAB_AT_HOME_PHLEBOTOMY_PARTIAL_RESULTS:
            return sample_with_lab_at_home_phlebotomy_partial_results()
        if self is OrderStatus.CANCELLED_AT_HOME_PHLEBOTOMY_CANCELLED:
            return cancelled_at_home_phlebotomy_cancelled()
        if self is OrderStatus.FAILED_AT_HOME_PHLEBOTOMY_SAMPLE_ERROR:
            return failed_at_home_phlebotomy_sample_error()
        if self is OrderStatus.RECEIVED_TESTKIT_ORDERED:
            return received_testkit_ordered()
        if self is OrderStatus.RECEIVED_TESTKIT_AWAITING_REGISTRATION:
            return received_testkit_awaiting_registration()
        if self is OrderStatus.RECEIVED_TESTKIT_REQUISITION_CREATED:
            return received_testkit_requisition_created()
        if self is OrderStatus.RECEIVED_TESTKIT_REGISTERED:
            return received_testkit_registered()
        if self is OrderStatus.COLLECTING_SAMPLE_TESTKIT_TRANSIT_CUSTOMER:
            return collecting_sample_testkit_transit_customer()
        if self is OrderStatus.COLLECTING_SAMPLE_TESTKIT_OUT_FOR_DELIVERY:
            return collecting_sample_testkit_out_for_delivery()
        if self is OrderStatus.COLLECTING_SAMPLE_TESTKIT_WITH_CUSTOMER:
            return collecting_sample_testkit_with_customer()
        if self is OrderStatus.COLLECTING_SAMPLE_TESTKIT_TRANSIT_LAB:
            return collecting_sample_testkit_transit_lab()
        if self is OrderStatus.SAMPLE_WITH_LAB_TESTKIT_DELIVERED_TO_LAB:
            return sample_with_lab_testkit_delivered_to_lab()
        if self is OrderStatus.COMPLETED_TESTKIT_COMPLETED:
            return completed_testkit_completed()
        if self is OrderStatus.FAILED_TESTKIT_FAILURE_TO_DELIVER_TO_CUSTOMER:
            return failed_testkit_failure_to_deliver_to_customer()
        if self is OrderStatus.FAILED_TESTKIT_FAILURE_TO_DELIVER_TO_LAB:
            return failed_testkit_failure_to_deliver_to_lab()
        if self is OrderStatus.FAILED_TESTKIT_SAMPLE_ERROR:
            return failed_testkit_sample_error()
        if self is OrderStatus.FAILED_TESTKIT_LOST:
            return failed_testkit_lost()
        if self is OrderStatus.CANCELLED_TESTKIT_CANCELLED:
            return cancelled_testkit_cancelled()
        if self is OrderStatus.CANCELLED_TESTKIT_DO_NOT_PROCESS:
            return cancelled_testkit_do_not_process()
