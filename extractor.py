import csv
from objs.event import new_event, Event
from objs.pateint import new_patient

patients = {}

with open('data/demo.psv', 'rb') as f:
  reader = csv.reader(f, delimiter="|")
  next(reader, None)
  for row in reader:
    patient = new_patient(row)

    if patient:
      patient[row[0]] = patient


with open('data/events.psv', 'rb') as f:
  reader = csv.reader(f, delimiter="|")
  next(reader, None)
  for row in reader:
    p_id = row[0]
    event = new_event(row)
    if event and p_id in patients:
      patients[p_id].add_event(event)

