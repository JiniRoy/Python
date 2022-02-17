
import datetime
current_datetime=datetime.datetime.now()
print('current date and time is ',current_datetime)

current_date=datetime.date.today()
print('current year ', current_date.year)
month = current_date.strftime("%B")
print('Month of year  ',month)
weeknum = current_datetime.strftime("%W")
print(' Weeknumber of the week',weeknum)
weekday = current_datetime.strftime("%w")
print(' Weekday of the week',weekday)
Day= current_date.strftime('%j')
print(' Day of year ' ,Day )
Daymonth=current_date.strftime('%d')
print('Day of the month',Daymonth)
Dayweek=current_date.strftime('%A')
print('Day of the week ',Dayweek)