import datetime
today = datetime.date(2026,6,18)
print(today)
time = datetime.time(7,0,0)
print(time)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

target_datetime = datetime.datetime(2026,6,18,7,7,30)
current_datetime = datetime.datetime.now()
if current_datetime > target_datetime:
    print("The timer has ended")
else:
    print("There is still some time left")