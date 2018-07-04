import pytest
import json
import objs.event as e
from objs.event import new_event, Event


def test_success_new_event(): 
  row = ("id-972", "2015-09-21", "9", "367.0")
  event = new_event(row)
  assert event != None
  assert event.system == e.SYSTEM_9
  assert event.date.strftime('%Y-%m-%d') == "2015-09-21"

  event_lkp = json.loads(event.to_json())
  assert event_lkp["date"] == "2015-09-21"
  assert event_lkp["system"] == e.SYSTEM_9
  assert event_lkp["code"] == "367.0"


def test_another_new_event(): 
  row = ("id-972", "2013-07-11", "10", "Z01.00")
  event = new_event(row)
  assert event != None
  assert event.system == e.SYSTEM_10
  assert event.date.strftime('%Y-%m-%d') == "2013-07-11"

  event_lkp = json.loads(event.to_json())
  assert event_lkp["date"] == "2013-07-11"
  assert event_lkp["system"] == e.SYSTEM_10
  assert event_lkp["code"] == "Z01.00"


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