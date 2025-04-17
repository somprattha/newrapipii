
import ephem
import datetime

def get_loikrathong_date(year):
    date = datetime.date(year, 11, 1)
    while True:
        moon = ephem.Moon()
        moon.compute(date.strftime('%Y/%m/%d'))
        next_full = ephem.next_full_moon(date)
        if next_full.datetime().month == 11:
            return next_full.datetime().date()
        else:
            date += datetime.timedelta(days=1)
