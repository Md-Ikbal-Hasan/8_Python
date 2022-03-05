
#tup = (1,2,3,'hello' , 9.84)
'''
print(tup)
print(type(tup))
print(tup[3])
print(tup[:3])
print(tup[1:4])
'''


'''  
new_list = list(tup)  # tuple to list convert...
print(new_list)
print(type(new_list))

T = tuple(new_list) # list to tuple convert...
print(T)
print(type(T))
'''


# ...........Reference............

import copy as cp

def func(some_list):
    some_list.append('ok')
    print("in function: " , some_list)

x = [1,2,3]
x2 = cp.copy(x)
func(x2)
print(x)

