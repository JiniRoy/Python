from datetime import date


from datetime import datetime
date='16/06/2015'
date_time=datetime.strptime(date,"%d/%m/%Y")
weekNum=date_time.strftime('%W')
print(weekNum)