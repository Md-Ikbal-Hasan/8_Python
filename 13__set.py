myList  = [12,34,56,78,34,543]
# set dont store duplicate value
s_from_list = set(myList)  # list to set
print(s_from_list)
print(type(s_from_list))

s_from_list.add(420)
print(s_from_list)

s_from_list.add(420)
print(s_from_list)

s_from_list.remove(56)
print(s_from_list)

print(len(s_from_list))

mySet = set()
mySet = {1,2,5,63,4,6756}
print(mySet)

mySet2 = set({12,34,56123123})
print(mySet2)

mySet3 = {12,34,'ikbal',23,12,34,10,'rahim'}
print(mySet3)
print(23 in mySet3)

num1 = {1,2,3,4,5,}
num2 = set([4,5,6,7])


print(num1 | num2)  # union operation.......

print(num1 & num2)  # interaction operation.......

print(num1 - num2)  # difference operation.......
