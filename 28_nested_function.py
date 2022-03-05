def outerFunction(text):
    def innerFunction():
        print("I am from inner Fucntion")
        print(text)
    return innerFunction()


outerFunction("Hello World")




def pop(list):
    def get_last_item(my_list):
        return my_list[len(list) - 1 ] #last item of list
    list.remove(get_last_item(list))
    return list


a = [12,34,56,78,90]
print(f'before pop: {a}')
print("after pop: ")

print(pop(a))
print(pop(a))
print(pop(a))
print(pop(a))


