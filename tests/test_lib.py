import lib
from datetime import datetime, timedelta


def test_calc_years():
  date1 = datetime.strptime("1981-01-02", '%Y-%m-%d') 
  date2 = datetime.strptime("1981-01-03", '%Y-%m-%d') 

  assert lib.calc_years(date1, date2) == 0
  assert lib.calc_years(date2, date1) == 0

  date2 = datetime.strptime("1982-01-01", '%Y-%m-%d') 
  assert lib.calc_years(date1, date2) == 0
  assert lib.calc_years(date1, date2 + timedelta(days=1)) == 1
  assert lib.calc_years(date2 + timedelta(days=1), date1) == 1


def test_cacl_aggs():
  list1 = [6, 4, 2, 1, 5, 8]
  list2 = [6, 4, 2, 1, 5, 8, 9]
  list3 = [3]

  assert lib.calc_aggs(None) == None
  assert lib.calc_aggs("string") == None
  assert lib.calc_aggs([]) == None

  assert lib.calc_aggs(list1) == (1, 8, 4.5)
  assert lib.calc_aggs(list2) == (1, 9, 5)
  assert lib.calc_aggs(list3) == (3, 3, 3)
