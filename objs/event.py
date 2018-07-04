import logging
from datetime import datetime

"""
# constants 
"""
IDX_DATE = 1
IDX_VERSION = 2
IDX_CODE = 3
ROW_LENGH = 4
SYSTEM_9 = "http://hl7.org/fhir/sid/icd-9-cm"
SYSTEM_10 = "http://hl7.org/fhir/sid/icd-10"


"""
# Event Class
"""
class Event:

  def __init__(self, date, system, code):
    self.date = date
    self.system = system
    self.code = code


def new_event(row):

  if len(row) < ROW_LENGH:
    # missing value
    return None

  if not (row[IDX_DATE] and row[IDX_VERSION] and row[IDX_CODE]):
    # empty field
    return None

  if row[IDX_VERSION] not in ["9", "10"]:
    # invalid version number
    return None

  system = SYSTEM_9 if row[IDX_VERSION] == "9" else SYSTEM_10
  date = None

  try: 
    date = datetime.strptime(row[IDX_DATE], '%Y-%m-%d') 
  except Exception as e:
    logging.debug("Invalid date str: %r", e)
    return None
  
  return Event(date, system, row[IDX_CODE])

  