import requests
from datetime import datetime as dt, timedelta
import pytz
from timezonefinder import TimezoneFinder

lat = float(input("Please enter the value of Latitude: "))
lon = float(input("Please enter the value of Longitude: "))
tz = pytz.timezone(TimezoneFinder().timezone_at(lng=lon, lat=lat))
dt_tz = dt(dt.now(tz).year, dt.now(tz).month, dt.now(tz).day, 4, tzinfo=tz)
utc_offset_delta = dt.now(tz).utcoffset().total_seconds() - dt_tz.utcoffset().total_seconds()
unix_timestamp = int((dt(dt.now(tz).year, dt.now(tz).month, dt.now(tz).day, 4, tzinfo=tz)
                     - timedelta(seconds=utc_offset_delta)).timestamp())

for i in range(1, 4):
    tm = unix_timestamp - (86400*i)
    res = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}'
                       '&appid=78385f931961ae9b80060c70d2c7bf6f'.format(lat, lon, tm))
    print(str(res.json()['current']['pressure']) + ' ' + 'Millibar')
