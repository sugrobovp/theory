def log_decorator(func):
    def wrapper(*args):
        print(f'Была вызвана функция {func.__name__} с параметрами {args}')
        result = func(*args)
        print(f'Результат: {result}')
        return result

    return wrapper


@log_decorator
def add(a, b):
    return a + b


@log_decorator
def multiply(x, y, z):
    return x * y * z


if __name__ == '__main__':
    add(5, 6)
    multiply(1, 4, 13)
