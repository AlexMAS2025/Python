import math

def debug(func, *args, **kwargs):
    if callable(func):
        print(f'Calling {func} with args {args} and kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'The result is {result}')

debug(math.factorial, 10)
