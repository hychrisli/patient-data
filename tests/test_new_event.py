import pytest
import objs.event as e
from objs.event import new_event, Event


def test_success_new_event(): 
  row = ("id-972", "2015-09-21", "9", "367.0")
  event = new_event(row)
  assert event != None
  assert event.system == e.SYSTEM_9
  assert event.date.strftime('%Y-%m-%d') == "2015-09-21"


def test_missing_value():
  row = ("2015-09-21", "9")
  assert new_event(row) == None


def test_invalid_date_format():
  row = ("id-972", "2015/09/21", "9", "367.0")
  assert new_event(row) == None


def test_invalid_date():
  row = ("id-972", "2015-09-45", "9", "367.0")
  assert new_event(row) == None


def test_invalid_version():
  row = ("id-972", "2015-09-12", "7", "367.0")
  assert new_event(row) == None