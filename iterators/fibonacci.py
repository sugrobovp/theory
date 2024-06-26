class FibonacciIterator:

    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.b

it = FibonacciIterator(50)

for num in it:
    print(num)


def fibonacci_generator():
    a, b = 0, 1
    for i in range(10):
        yield a
        a, b = b, a + b


for num in fibonacci_generator():
    print(num)
