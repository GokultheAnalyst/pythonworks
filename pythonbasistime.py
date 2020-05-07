from datetime import datetime
from datetime import date as dt
from datetime import time as tm
from datetime import timedelta as td

dtval='2020-04-10 10:10:19 PM'
## convert a string variable into date value

dtvald=datetime.strptime(dtval,"%Y-%m-%d %I:%M:%S %p" )
dtvald1=datetime.strftime(dtvald,"%Y-%m-%d %I:%M:%S %p" )
print(type(dtval),dtvald,type(dtvald),dtvald1)
