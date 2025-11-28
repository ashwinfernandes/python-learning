import datetime as dt
from datetime import datetime

today = dt.datetime.today()
now = datetime.now()
utc_now = datetime.utcnow() # utcnow is deprecated

print(today)
print(now)
print(utc_now)
