

def limiter(calls: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func.calls_count = getattr(func, 'calls_count', 0)
            if func.calls_count >= calls:
                raise ValueError(f'Function already called {calls} times')

            result = func(*args, **kwargs)
            func.calls_count += 1

            return result
        return wrapper
    return decorator


@limiter(1)
def sum_number(num1: float, num2: float):
    print('calling sum numbers')
    return num1 + num2


def hello(name):
    print(f'hello, {name}')


def main():
    hello('peter')
    sum_number(1, 2)
    sum_number(1, 2)


if __name__ == '__main__':
    main()
