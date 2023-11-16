def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if not args in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]

    return wrapper


@cache_decorator
def sum(x, y):
    print(f'Calling sum with {x} and {y}')
    return x + y


print(sum(5, 6))
print(sum(5, 6))
print(sum(5, 6))
print(sum(5, 6))
