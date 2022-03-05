"""
#key value pair....
my_stuff = {'book':'C programming' , 'phone':'iphone' , 'Home':'Bangladesh'}
print(my_stuff)
print(my_stuff['phone'])

x = {0:100 , 1:200 , 2:300 , 3:400}
print(x[1])
"""


""" 
a = [1,2,3]
b = [2,3,1]
print(a==b)  # False

c = {1:100 , 2:200}
d = {2:200 , 1:100}
print(c==d)   # True
"""


D = {'a':100  ,'b':200}
E = {'c':300 , 'd':400}
new_dic = D.copy()  # copy
print(new_dic)

new_dic.update(E)
print(new_dic)  # concate


