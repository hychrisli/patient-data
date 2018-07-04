import pytest
import logging
import json
import objs.patient as p
from objs.patient import new_patient, Patient
from objs.event import new_event


@pytest.fixture(scope="module")
def patient_a():
  return new_patient(("id-771", "1981-12-20", "F"))


@pytest.fixture(scope="module")
def event_a():
  return new_event(("id-771","2015-09-21", "9", "367.0"))


def test_success_patient(caplog):
  caplog.set_level(logging.DEBUG)
  row = ("id-771", "1981-12-20", "M")
  patient = new_patient(row)

  assert patient != None
  assert patient.gender == "M"
  assert patient.birth_date.strftime('%Y-%m-%d') == "1981-12-20"

  patient_lkp = json.loads(patient.to_json())
  assert patient_lkp["birth_date"] == "1981-12-20"
  assert patient_lkp["gender"] == "M"


def test_none():
  assert new_patient(None) == None


def test_missing_values():
  assert new_patient(("id-771", "1981-12-20")) == None


def test_empty_fields():
  assert new_patient(("id-771", "", "M")) == None
  assert new_patient(("id-771", "1981-12-20", "")) == None


def test_invalid_gender():
  assert new_patient(("id-771", "1981-12-20", "T")) == None


def test_invalid_birth_date_format():
  assert new_patient(("id-771", "1981/12,20", "M")) == None


def test_invalid_birth_date():
  assert new_patient(("id-771", "1981-12-32", "M")) == None


def test_add_event_none(patient_a):
  patient_a.add_event(None)
  assert patient_a.is_active() == False


def test_add_not_event(patient_a):
  patient_a.add_event(["not event"])
  assert patient_a.is_active() == False


def test_add_event_success(patient_a, event_a):
  patient_a.add_event(event_a)
  assert patient_a.is_active()

  patient_lkp = json.loads(patient_a.to_json())

  assert patient_lkp["birth_date"] == "1981-12-20"
  assert patient_lkp["events"][0]["date"] == "2015-09-21"

