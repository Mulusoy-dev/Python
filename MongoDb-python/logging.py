def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        for arg in args:
            return function(*args, **kwargs)
        function()
    return wrapper_function


@logging_decorator
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add(1, 2, 3))
