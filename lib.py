from datetime import date


def calc_years(date1, date2):
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

