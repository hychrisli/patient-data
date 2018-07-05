import csv
import os
import json
import logging
import argparse

import lib
from objs.event import new_event, Event
from objs.patient import new_patient
from const import RESULTS_DIR, EVENT_DATA, PATIENT_DATA


"""
# Module methods
"""
def setup():
  """
  #  set up the project. Checking and creating results directory
  """
  if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)


def gen_patients():
  """
  # Read data from file and create patient and event object line by line
  """
  patients = {}
  
  with open(PATIENT_DATA, 'rb') as f:
    reader = csv.reader(f, delimiter="|")
    next(reader, None)
    
    for row in reader:
      patient = new_patient(row)

      if patient:
        patients[row[0]] = patient

  logger.info("Loaded patients data")

  with open(EVENT_DATA, 'rb') as f:
    reader = csv.reader(f, delimiter="|")
    next(reader, None)
    
    for row in reader:
      p_id = row[0]
      event = new_event(row)
      
      if event and p_id in patients:
        # if it's a valid event and it has a matching patient
        patients[p_id].add_event(event)

  logger.info("Loaded events data")

  return patients


def extract(patients):
  """
  # loop through patients dictionary
  # output JSON files for valid patients
  # calcuate statistics
  """
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

      outfile = RESULTS_DIR + pid + ".json"
      with open(outfile, "wb") as f:
        f.write(patient.to_json())

  logger.info("Generated Patient JSON files in results folder")

  min_timeline, max_timeline, median_timeline = lib.calc_aggs(timelines)
  min_age, max_age, median_age = lib.calc_aggs(ages)

  stats["min_timeline"] = "%d days" % min_timeline
  stats["max_timeline"] = "%d days" % max_timeline
  stats["median_timeline"] = "%d days" % median_timeline
  stats["min_last_event_age"] = "%d years" % min_age
  stats["max_last_event_age"] = "%d years" % max_age
  stats["median_last_event_age"] = "%d years" % median_age

  outfile = RESULTS_DIR + "stats.json"
  with open(outfile, "wb") as f: 
    f.write(json.dumps(stats, indent=4, sort_keys=True))

  logger.info("Wrote statistics to results/stats.json")


"""
#  Main
"""
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Parsing arguments')
  parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
  args = parser.parse_args()

  numeric_level = logging.DEBUG if args.verbose else logging.INFO
  logger = lib.get_root_logger(__name__, numeric_level)
  
  setup()
  extract(gen_patients())