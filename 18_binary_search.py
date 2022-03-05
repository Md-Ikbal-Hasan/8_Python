# binary_search work on sorted list......
def binary_search(list_of_number , value):

    if value> list_of_number[-1]:
        return "not found"

    first_index = 0
    last_index = len(list_of_number)

    while first_index <= last_index:
        mid = (first_index + last_index)//2

        if list_of_number[mid] == value:
            return value , " Found at index" , mid
        elif list_of_number[mid] <value:
            first_index = mid + 1
        elif list_of_number[mid] > value:
             last_index = mid - 1

    if first_index> last_index:
        return 'not found'



numbers = [12,23,34,45,67,89]
searching_element = 34
result = binary_search(numbers , searching_element)
print(result)

