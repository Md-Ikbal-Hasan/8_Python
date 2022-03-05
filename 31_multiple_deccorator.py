'''
Decorator wrap the function and modify its behaviour in one way
or another without having to directly change th source the code of
the function being decorated
'''

def decorator_x(func):
    def wrapper_func():
        print('x' * 20)
        func()
        print('x' * 20)

    return wrapper_func



def decorator_y(func):
    def wrapper_func():
        print('y' * 20)
        func()
        print('y' * 20)

    return wrapper_func

#@decorator_x
#@decorator_y
def say_hello():
    print("Hello World")

hello = decorator_x(decorator_y(say_hello))
hello()

#say_hello( )

