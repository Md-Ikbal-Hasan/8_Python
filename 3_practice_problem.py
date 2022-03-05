# problem 1 swapping value
''' 
a = input()
b = input()
print("a = " + a + "\n" + "b = "+ b)
temp = a
a = b
b = temp
print("after swapping: ")
print("a = " + a + "\n" + "b = "+ b) 
'''


#problem 2 find the value of x ....   x = (-b +- sqrt(b*2-4ac)) / 2*a
""" 
import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d =  math.sqrt( b*b - 4*a*c)
x1 = (-b + d) / 2*a
x2 = (-b -d) / 2*a
print("x =  " + str(x1))
print("x = " + str(x2))
"""

#problem 3 celcius to farenheit
c = int(input("c = "))
f = (9/5)*c + 32
print(f)
 