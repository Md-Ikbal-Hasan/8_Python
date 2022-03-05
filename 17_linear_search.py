# Linear search..........
def linear_search(list_of_number , x):
    flag = False
    length = len(list_of_number)
    for i in range(length):
        if list_of_number[i]==x:
            flag = True
            return flag
    return flag



numbers = [12,45,23,67,34,89]
searching_element = 18

result = linear_search(numbers , searching_element)
if result:
    print("Yes")
else:
    print("No")

