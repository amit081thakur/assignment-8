


#question2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


import time
localtime = time.asctime(time.localtime(time.time()))
print("local current time:",localtime)
local current time: Wed Jun 13 21:19:32 2018
 

#question 3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>>
import calendar
for i in range(3):
	year = int(input("enter the year:"))
	month= int(input("enter month:"))
	mont = calendar.month(year,month)
	print("calender:",mont)
# question 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>.
import datetime

from datetime import date
print("the calculated date from second is:",end="")
print(date.fromtimestamp(2345674))



#question 5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

d = datetime.date.today()
d.month
d.day
d.year

#question 6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import time

print("time:",time.localtime())

#question 7>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import math

math.factorial(3)
math.factorial(45)
math.factorial(2)


#question 8>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

for i in range(5):
	a = int(input("enter 1st number:"))
	b = int(input("enter 2nd number:"))
	print(math.gcd(a,b))


#question 9 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	
import time
import os
import math

print("current working directory>>>>>>>>>>>>", get.cwd())
print(" current user environment>>>>>>>>>>>>X", os.environ)
 
