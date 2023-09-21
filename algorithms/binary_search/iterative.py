def iterative_binary_search(arr: list, el: int) -> int:
    length = len(arr)
    i = 0
    j = length - 1

    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == el:
            return mid
        elif arr[mid] > el:
            j = mid - 1
        elif arr[mid] < el:
            i = mid + 1

    return -1


a = [1, 4, 5, 8, 9, 25, 47]
print(iterative_binary_search(a, 47))

