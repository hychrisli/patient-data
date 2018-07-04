import csv
from objs.event import new_event, Event

events = [] 

with open('data/events.psv', 'rb') as f:
  reader = csv.reader(f, delimiter="|")
  next(reader, None)
  events = map(tuple, reader)

print events