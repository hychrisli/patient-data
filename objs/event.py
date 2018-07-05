import logging
import json
from datetime import datetime
from const import IDX_DATE, IDX_VERSION, IDX_CODE, EVENT_ROW_LENGH, SYSTEM_9, SYSTEM_10


"""
# Event Class
"""
class Event:
  """
  # Event class store data, system and code info
  """
  
  def __init__(self, date, system, code):
    self.date = date
    self.system = system
    self.code = code


  def to_dict(self):
    return {
      "date": self.date.strftime('%Y-%m-%d'),
      "system": self.system,
      "code": self.code
    }


  def to_json(self):
    return json.dumps(self.to_dict())


"""
# Module Methods
"""
def new_event(row):

  if not row or len(row) < EVENT_ROW_LENGH:
    logging.debug("[NEW_EVENT] Input None or missing values: %r", row)
    return None

  if not (row[IDX_DATE] and row[IDX_VERSION] and row[IDX_CODE]):
    logging.debug("[NEW_EVENT] Empty fields: %r", row)
    return None

  if row[IDX_VERSION] not in ["9", "10"]:
    logging.debug("[NEW_EVENT] Invalid version: %r", row)
    return None

  system = SYSTEM_9 if row[IDX_VERSION] == "9" else SYSTEM_10
  date = None

  try: 
    date = datetime.strptime(row[IDX_DATE], '%Y-%m-%d') 
  except Exception as e:
    logging.debug("[NEW_EVENT] Invalid date string: %r", e)
    return None
  
  return Event(date, system, row[IDX_CODE])

  