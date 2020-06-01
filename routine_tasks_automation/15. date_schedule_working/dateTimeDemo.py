import datetime
import time


now_time = time.time()
print(datetime.datetime.fromtimestamp(now_time))

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
print(halloween2015 < newyears2016)

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.total_seconds())

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirstyYears = datetime.timedelta(days=365 * 30)
print(oct21st - aboutThirstyYears)

print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime('%B of %y'))

# Строки в объект
strToObj = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(strToObj)
strToObj = datetime.datetime.strptime('2015/10/21 16:29', '%Y/%m/%d %H:%M')
print(strToObj)
