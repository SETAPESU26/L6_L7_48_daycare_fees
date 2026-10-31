import pytest
from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status
)


# --------------------------------
# EXTRA HOURS FEE TESTS
# --------------------------------

def test_unknown_age_group():
    with pytest.raises(ValueError):
        extra_hours_fee("school", 30, False)


def test_negative_hours():
    with pytest.raises(ValueError):
        extra_hours_fee("toddler", -1, False)


def test_within_included_hours():
    assert extra_hours_fee("toddler", 20, False) == 0


def test_infant_extra_hours():
    assert extra_hours_fee("infant", 25, False) == 70


def test_toddler_extra_hours():
    assert extra_hours_fee("toddler", 30, False) == 45


def test_sibling_discount():
    assert extra_hours_fee("toddler", 31, True) == 9


def test_infant_sibling_no_discount():
    assert extra_hours_fee("infant", 25, True) == 70


def test_high_extra_hours():
    assert extra_hours_fee("toddler", 50, False) == 350


def test_infant_high_extra_hours():
    assert extra_hours_fee("infant", 45, False) == 550


# --------------------------------
# ENROLMENT TESTS
# --------------------------------

def test_enrolment_pending_allowed():
    assert enrolment_allowed(12, 0, True) is True


def test_enrolment_pending_not_allowed():
    assert enrolment_allowed(10, 2, True) is False


def test_enrolment_age_below_six():
    assert enrolment_allowed(5, 2, False) is False


def test_enrolment_with_vacancy():
    assert enrolment_allowed(12, 2, False) is True


def test_enrolment_without_vacancy():
    assert enrolment_allowed(12, 0, False) is False


# --------------------------------
# PICKUP STATUS TESTS
# --------------------------------

def test_pickup_on_time():
    assert pickup_status(20, False, False) == "on_time"


def test_pickup_late():
    assert pickup_status(5, False, False) == "late"


def test_pickup_overdue():
    assert pickup_status(-6, False, False) == "overdue"


def test_aftercare_pickup():
    assert pickup_status(20, True, False) == "on_time"


def test_friday_pickup():
    assert pickup_status(20, False, True) == "on_time"


def test_aftercare_friday_pickup():
    assert pickup_status(30, True, True) == "on_time"