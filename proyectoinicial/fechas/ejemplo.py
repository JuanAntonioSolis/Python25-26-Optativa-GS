from datetime import datetime,date

now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

t = now.strftime("%H:%M:%S")
print(t)

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)

fecha = date(2025,10,20)
print(fecha.strftime("%d/%m/%y"))

fechahoy = date.now()
fechanac = date(year=2000,month=10,day=10)
diff = fechahoy - fechanac
print(diff.days)