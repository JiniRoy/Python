import datetime
Date=datetime.date.today()
day=Date.day
newday=day-5
newdate=datetime.date(Date.year,Date.month,newday)
print('current date ',Date)
print('Date before 5 days ',newdate)


