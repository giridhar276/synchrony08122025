
# method1 : all the methods are imported to the program space
import math 
print(math.tan(1))
print(math.log(1))
print(dir(math))


# method2 : importing with alias name
import math as m 
print(m.floor(34.3))





#method3  : importing required methods only
from math import cos,sin 
print(cos(1))
print(sin(2))

