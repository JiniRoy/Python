from datetime import date

t1=date(day=28,month=2,year=2000)
t2=date(day=28, month=2,year=2001)
t3=t2-t1
print(t3.days)