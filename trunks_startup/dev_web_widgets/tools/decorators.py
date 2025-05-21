import os
import time

from decorator import decorator


@decorator
def check_arguments(func, *args, **kw):

    return func(*args, **kw)

# --------- Simple decorator
def printres(func): # decorator name, wrapped function receiver

    def handler(*args, **kwargs): # decorator handling function
        res = func(*args, **kwargs)
        print("{}: {}".format("Result", res))
        return res
    return handler


import functools

def printmsg(message): # decorator name, decorator parameters

    def function_receiver(func): # wrapped function receiver
        @functools.wraps(func) # munge func so that stack traces and call sequences are retained

        def handler(*args, **kwargs): # decorator handling function
            res = func(*args, **kwargs)
            print("{}: {}".format(message, res))
            return res
        return handler
    return function_receiver

# ----------- Usage demo

@printres
def plus(x, y):
    return x+y


@printmsg("minus")
def minus(x, y):
    return x-y

def print_me(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(kwargs) > 0:
            print("\n{}{}{} = {}".format(func.__name__, args, kwargs, result))
        else:
            print("\n{}{} = {}".format(func.__name__, args, result))
        return result
    return wrapper



@print_me
def add(x, y):
    return x+y


@print_me
def multiply_by_two(x):
    return add(x, x)


@print_me
def nothing():
    pass


if __name__ == '__main__':
    z1 = plus(2, 3)
    z2 = minus(3, 6)

    print("Final print: {} // {} ".format(z1, z2))
    add(2, 3)
    multiply_by_two(5)
    nothing()