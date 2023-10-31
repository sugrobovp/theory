import time
from time import sleep


def limiter(func):
    def wrapper(*args, **kwargs):
        func.calls_count = getattr(func, 'calls_count', 0)

        if func.calls_count >= 3:
            time.sleep(1)
            func.calls_count = 0

        result = func(*args, **kwargs)
        func.calls_count += 1

        return result

    return wrapper


@limiter
def sum_number(num1: float, num2: float):
    print('calling sum numbers')
    return num1 + num2


def hello(name):
    print(f'hello, {name}')


def main():
    hello('peter')
    for i in range(10):
        sum_number(1, 2)


if __name__ == '__main__':
    main()
