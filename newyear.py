#install dateutil- pip install python-dateutil
#relativedelta is used to find the interval between the dates

from dateutil.relativedelta import relativedelta
from datetime import datetime
dt=datetime.today()
print("Today:",dt) # current date and time 
print(" No of days left for New year")
dt2 = datetime(dt.year+1,1,1,0,0,0) # Date and time for new year
dt3 = relativedelta(dt2,dt) # time left for new year 
print("Years:", dt3.years, ", Months:",dt3.months, "Days:",dt3.days,
    ",Hours :",dt3.hours,", Minutes :",dt3.minutes, ", Seconds :",dt3.seconds)
