from datetime import datetime
import calendar

d, m = input().split()
date_str = d + '/' + m + '/09 00:00:00'

date = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S')
print(calendar.day_name[date.weekday()])
