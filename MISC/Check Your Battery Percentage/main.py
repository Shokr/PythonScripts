import psutil

battery = psutil.sensors_battery()
percent = str(battery.percent)

print("Battery Percent= " + percent + "%")
