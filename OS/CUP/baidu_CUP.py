# Examples:
# 1. Get system info
import json

import cup
from cup import exfile
from cup.net import route
from cup.res import linux
# count cpu usage in interval, by default 60 seconds

cpuinfo = linux.get_cpu_usage(intvl_in_sec=60)
print(cpuinfo.usr)

# total, available, percent, used, free, active, inactive, buffers, cached

meminfo = linux.get_meminfo()
print(meminfo.total)
print(meminfo.available)

# http://cup.iobusy.com/api-ref/

print(cup.res.linux.boot_time())

print(cup.res.linux.get_disk_info())

ri = route.RouteInfo()
print(json.dumps(ri.get_routes(), indent=1))

# Lock file in order to prevent others from trying to lock it again

filelock = exfile.LockFile("requirments.txt", locktype=2)
# xxxx do something
filelock.lock(blocking=True)
# xxxxx do something else
filelock.unlock()
