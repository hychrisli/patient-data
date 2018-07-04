import csv
import lib
from objs.event import new_event, Event
from objs.patient import new_patient


"""
# Module methods
"""
def gen_patients():

  patients = {}
  
  with open('data/demo.psv', 'rb') as f:
    reader = csv.reader(f, delimiter="|")
    next(reader, None)
    
    for row in reader:
      patient = new_patient(row)

      if patient:
        patients[row[0]] = patient


  with open('data/events.psv', 'rb') as f:
    reader = csv.reader(f, delimiter="|")
    next(reader, None)
    
    for row in reader:
      p_id = row[0]
      event = new_event(row)
      
      if event and p_id in patients:
        patients[p_id].add_event(event)

  return patients


def extract(patients):

  stats = {
    "patients": 0,
    "males": 0,
    "females": 0
  }

  timelines = []
  ages = []

  for pid in patients:
    patient = patients[pid]

    if patient.is_active():
      stats["patients"] += 1

      if patient.gender == "M":
        stats["males"] += 1
      else: 
        stats["females"] += 1

      timelines.append(patient.get_timeline_length())
      ages.append(patient.get_last_visit_age())

  min_timeline, max_timeline, median_timeline = lib.calc_aggs(timelines)
  min_age, max_age, median_age = lib.calc_aggs(ages)

  stats["min_timeline"] = min_timeline
  stats["max_timeline"] = max_timeline
  stats["median_timeline"] = median_timeline
  stats["min_last_event_age"] = min_age
  stats["max_last_event_age"] = max_age
  stats["median_last_event_age"] = median_age

  print stats


"""
#  Main
"""
if __name__ == "__main__":
  extract(gen_patients())