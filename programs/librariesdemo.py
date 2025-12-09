
import os 
for file in os.listdir():
    print(file)

# if directory is not existing only .. then its created created
if not os.path.isdir("mydir"):
    os.mkdir("mydir")

import datetime 
print(datetime.datetime.now())

import time 
print(time.ctime())


import random 
print(random.randrange(1000,9999))


# pip install psutil 
import psutil 
print(psutil.cpu_percent())


import calendar
print(calendar.calendar(2025))