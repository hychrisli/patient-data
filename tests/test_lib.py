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