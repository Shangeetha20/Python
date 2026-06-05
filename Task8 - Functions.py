#Math Function
import math
print(math.pi)
print(math.sqrt(16))
print(math.acos(1))
print(math.atan(90))
print(math.ceil(8.4))
print(math.degrees(7))
print(math.factorial(6))
print(math.exp(2))
print(math.exp2(4))
print(math.expm1(9))
print(math.fabs(8))
print(math.floor(78))
print(math.gamma(5))
print(math.gcd(8,12))
print(math.hypot(3,4))
print(math.inf)
print(math.isqrt(7))
print(math.lcm(20,120))
print(math.log(5))
print(math.log10(5))
print(math.modf(89.56))
print(math.nan)

#Scipy Function
import scipy.constants as a

print(a.gram)
print(a.hour)
print(a.degree)

#Time Function
import time as t
print("Python")
t.sleep(10)
print("DS")
print(t.ctime(20))
print(t.strftime("%y"))
print(t.strftime("%y:%m"))
print(t.strftime("%y:%m:%d"))
print(t.strftime("%A"))
print(t.strftime("%d-%m-%Y"))
print(t.strftime("%H:%M:%S"))

#Calender Function
import calendar as c
print(c.calendar(2024))
print(c.month(2025,8))
print(c.isleap(2025))
print(c.isleap(2028))
print(c.leapdays (2000,2030))
print(c.weekday(2025,8,11))
print(c.monthcalendar(2025,7))
print(c.monthrange(2025,11))

#Filter
num=[4,24,7,28,8,11,20,25]
even=list(filter(lambda x:x%2==0, num))
print(even)

#Mapping
num=[1,2,3,4,5,6]
sqt=list(map(lambda x :x**2,num))
print(sqt)

#Mapping & Filtering
nums=[1,3,8,14,17,23,32]
even=list(map(lambda x:x**2,filter(lambda x:x%2==0,nums)))
print(even)

#Counting variable in string
a=['apple','banana','kiwi','orange']
l=list(map(lambda x:len(x),a))
print(l)
