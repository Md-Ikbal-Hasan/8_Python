"""
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)


print( factorial(5) ) # 5! = 120


def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)

print( sum(4) )  # n=4 => 1+2+3+4 = 10
"""


# without recursion , reverse list......
def reverse_list(A):
    new_list= []
    length = len(A)
    for i in range(0,length):
        new_list.append(0)
    for i in range( len(A)-1 , -1  , -1):
        new_list[len(A)-1 -i] = A[i]
    return new_list

myList = [1,2,3,4]
print(myList)
print(reverse_list(myList))























