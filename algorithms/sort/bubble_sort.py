def bubble_sort(x: list) -> list:
    length = len(x)
    for i in range(length):
        for j in range(length - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


a = [1, 3, -1, 5, 2351, -100, -2, 15, 14]
print(bubble_sort(a))
