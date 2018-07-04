import csv
import json
from datetime import datetime
from objs.event import new_event
from objs.patient import new_patient
from const import *


"""
#  Events
"""
uniq_events = set()
patients_with_events = set()

event_stats = {
  "rows": 0,
  "uniq_events": 0,
  "missing_fields": 0, 
  "empty_fields": 0,
  "empty_id": 0,
  "empty_date": 0,
  "empty_version": 0,
  "empty_code": 0,
  "wrong_date": 0,
  "versions": set()
}

with open('data/events.psv', 'rb') as f:
  reader = csv.reader(f, delimiter="|")
  next(reader, None)
  for row in reader: 
    event_stats["rows"] += 1

    if len(row) < EVENT_ROW_LENGH:
      event_stats["missing_fields"] += 1
      print("missing fiels: %r" % row)
      continue

    if any( not elem for elem in row ):
      event_stats["empty_fields"] += 1

      if not row[IDX_ID]:
        event_stats["empty_id"] += 1

      if not row[IDX_DATE]:
        event_stats["empty_date"] += 1

      if not row[IDX_VERSION]:
        event_stats["empty_version"] += 1

      if not row[IDX_CODE]:
        event_stats["empty_code"] += 1

      continue

    key = ",".join([elem.strip().lower() for elem in row] )
    
    if key in uniq_events: 
      print ("key_already exists: %s, %r" % (key, row))
    else:
      uniq_events.add(key)

    patients_with_events.add(row[IDX_ID].strip().lower())
    event_stats["versions"].add(row[IDX_VERSION])

    try: 
      date = datetime.strptime(row[IDX_DATE], '%Y-%m-%d')
    except Exception as e: 
      print ("wrong date: %r", row)
      event_stats["wrong_date"] += 1


event_stats["uniq_events"] = len(uniq_events)
print ("event stats: %r" % event_stats)


"""
#  Patients
"""

uniq_patients = set()
patient_stats = {
  "rows": 0, 
  "uniq_patients": 0,
  "missing_fields": 0, 
  "empty_fields": 0,
  "empty_id": 0,
  "empty_birth_date": 0,
  "empty_gender": 0,
  "wrong_birth_date": 0,
  "genders": set()
}

with open('data/demo.psv', 'rb') as f:
  reader = csv.reader(f, delimiter="|")
  next(reader, None)
  for row in reader: 
    patient_stats["rows"] += 1

    if len(row) < PATIENT_ROW_LENGH:
      patient_stats["missing_fields"] += 1
      print("missing fiels: %r" % row)
      continue

    if any( not elem for elem in row ):
      patient_stats["empty_fields"] += 1

      if not row[IDX_ID]:
        patient_stats["empty_id"] += 1

      if not row[IDX_BIRTH_DATE]:
        patient_stats["empty_birth_date"] += 1

      if not row[IDX_GENDER]:
        patient_stats["empty_gender"] += 1

      continue

    key = row[0].strip().lower()
    
    if key in uniq_events: 
      print ("key_already exists: %s, %r" % (key, row))
    else:
      uniq_patients.add(key)

    patient_stats["genders"].add(row[IDX_GENDER])

    try: 
      date = datetime.strptime(row[IDX_BIRTH_DATE], '%Y-%m-%d')
    except Exception as e: 
      print ("wrong birth date: %r", row)
      patient_stats["wrong_birth_date"] += 1

patient_stats["uniq_patients"] = len(uniq_patients)

print "patient stats: %r" % patient_stats

patients_with_no_events = len(uniq_patients.difference(patients_with_events))

print "patients with no events: %d" % patients_with_no_events
print "valid patients: %d" % (patient_stats["uniq_patients"] - patients_with_no_events)
print "events with no patients: %d" % len(patients_with_events.difference(uniq_patients))