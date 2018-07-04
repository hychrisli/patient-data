from datetime import date


def calc_years(date1, date2):
  """
  # Calcluate years between two given dates
  """
  if not ( isinstance(date1, date) and isinstance(date2, date)):
    return -1

  if date1 > date2: 
    date_tmp = date1
    date1 = date2
    date2 = date_tmp

  years = date2.year - date1.year

  if date2.month < date1.month \
    or (date2.month == date1.month and date2.day < date1.day):
    years -= 1

  return years


def calc_aggs(mylist):
  """
  # Calculate min, max and median of a list of numbers
  """
  if not (mylist and isinstance(mylist, list)):
    return None

  mylist.sort()
  n = len(mylist)

  min_val = mylist[0]
  max_val = mylist[n-1]

  if n % 2 == 1:
    median_val = mylist[n/2]
  else:
    median_val = ( mylist[n/2] + mylist[(n-1)/2] ) / 2.0

  return min_val, max_val, median_val


