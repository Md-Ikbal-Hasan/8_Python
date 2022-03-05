def test():
    print("test done")
#test()


def sum(a,b):
    sum = a+b
    return sum
a=  sum(12,15)
#print(a)

def fibonacci(n):
    if n==0:
        return 0
    else:
        x =0
        y = 1
        print(x , end=" ")
        print(y, end=" ")
        for i in range(1,n-1):
            z = x+y
            x = y
            y = z
            print(z ,end=" ")

n  = int(input("enter the number of terms: ")) #n = 4  => 0 1 1 2
fibonacci(n)

import random as r


