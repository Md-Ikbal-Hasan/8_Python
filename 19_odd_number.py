

def odd_number(numbers):
    length = len(numbers)
    for i in range(length):
        if numbers[i] %2 !=0:
            print(i , end=" ")



numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odd_number(numbers)
