def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


a = [1, 3, -1, 5, 2351, -100, -2, 15, 14]
print(quick_sort(a))
