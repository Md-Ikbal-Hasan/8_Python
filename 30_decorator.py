'''
Decorator wrap the function and modify its behaviour in one way
or another without having to directly change the source the code of
the function being decorated
'''


def decorator_func(func):
    def wrapper_func():
        print('x' * 20)
        func()
        print('y' * 20)

    return wrapper_func


@decorator_func
def say_hello():
    print("Hello World")

#hello = decorator_func(say_hello)
#hello()

say_hello()


def decorator_divide(func):
    def wrapper_func(a,b):
        print(f'divide {a} and {b}')
        if b==0:
            return "zero division error"


        return a/b

    return wrapper_func


@decorator_divide
def divide(x,y):
    return x/y

print(divide(15,0))

#division =  decorator_divide(divide)
#print(division(15,0))






