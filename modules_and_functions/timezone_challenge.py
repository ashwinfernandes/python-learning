import zoneinfo
from datetime import datetime, timezone

timezones = {
    'Paris': 'Europe/Paris',
    'London': 'Europe/London',
    'Hong Kong': 'Asia/Hong_Kong',
    'Nairobi': 'Africa/Nairobi',
}

# utc_now = datetime.now(timezone.utc)
# for city, tz_name in timezones.items():
#     zone_info = zoneinfo.ZoneInfo(tz_name)
#     city_time = utc_now.astimezone(tz=zone_info).replace(microsecond=0)
#     print(f"The date and time in {city} is {city_time} {city_time.tzname()}")

for city, tz_name in timezones.items():
    # city_time = datetime.now().astimezone(zoneinfo.ZoneInfo(tz_name)).replace(microsecond=0)
    # city_time = datetime.now(zoneinfo.ZoneInfo(tz_name)).replace(microsecond=0)
    city_time = datetime.now(zoneinfo.ZoneInfo(tz_name))
    print(f"The date and time in {city} is {city_time} {city_time.tzname()}")
    # print(f"The date and time in {city} is {city_time.strftime("%m/%d/%Y %H:%M:%S %z %Z")} ")
