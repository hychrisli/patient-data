import pytest
import logging
import json
from objs.patient import new_patient, Patient
from objs.event import new_event


@pytest.fixture(scope="module")
def patient_a():
  patient_a = new_patient(("id-771", "1981-12-20", "F"))
  patient_a.add_event(new_event(("id-771", "2003-09-24", "10", "t023.0")))
  patient_a.add_event(new_event(("id-771", "2015-09-21", "9", "367.0")))
  patient_a.add_event(new_event(("id-771", "2018-03-23", "10", "z23.0")))
  patient_a.add_event(new_event(("id-771", "2008-10-01", "10", "d023.0")))
  patient_a.add_event(new_event(("id-771", "2001-05-16", "9", "b104.0")))

  return patient_a


def test_min_event_time(patient_a):
  assert patient_a.min_event_date.strftime('%Y-%m-%d') == "2001-05-16"


def test_max_event_time(patient_a):
  assert patient_a.max_event_date.strftime('%Y-%m-%d') == "2018-03-23"


def test_timeline_length(patient_a):
  assert patient_a.get_timeline_length() == 6155


def test_last_visit_age(patient_a):
  assert patient_a.get_last_visit_age() == 36

