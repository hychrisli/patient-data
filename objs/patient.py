import json
import logging
from datetime import datetime
from event import Event
from lib import calc_years
from const import IDX_BIRTH_DATE, IDX_GENDER, PATIENT_ROW_LENGH, MAX_DATE, MIN_DATE


"""
# Class
"""
class Patient:

  def __init__(self, birth_date, gender):
    self.birth_date = birth_date
    self.gender = gender
    self.events = []
    self.event_num = 0
    self.min_event_date = MAX_DATE
    self.max_event_date = MIN_DATE


  def add_event(self, event):
    if event and isinstance(event, Event):
      self.events.append(event.to_dict())
      self.min_event_date = min(self.min_event_date, event.date)
      self.max_event_date = max(self.max_event_date, event.date)
      self.event_num += 1


  def get_timeline_length(self):
    return (self.max_event_date - self.min_event_date).days


  def get_last_visit_age(self):
    return calc_years(self.birth_date,  self.max_event_date)


  def is_active(self):
    return self.event_num > 0


  def to_dict(self):
    return {
      "birth_date": self.birth_date.strftime('%Y-%m-%d'),
      "gender": self.gender,
      "events": self.events
    }

  def to_json(self):
    return json.dumps(self.to_dict())


"""
# Module Methods
"""
def new_patient(row):

  if not row or len(row) < PATIENT_ROW_LENGH:
    logging.debug("[NEW_PATIENT] Input None or missing values: %r", row)
    return None

  if not ( row[IDX_BIRTH_DATE] and row[IDX_GENDER] ):
    logging.debug("[NEW_PATIENT] Empty fields: %r", row)
    return None

  if row[IDX_GENDER] not in ["M", "F"]:
    logging.debug("[NEW_PATIENT] Invalid gender: %r", row)
    return None

  birth_date = None
  try: 
    birth_date = datetime.strptime(row[IDX_BIRTH_DATE], '%Y-%m-%d') 
  except Exception as e:
    logging.debug("[NEW_PATIENT] Invalid birthday str: %r", e)
    return None

  return Patient(birth_date, row[IDX_GENDER])
