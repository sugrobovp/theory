def recursive_binary_search(arr: list, el: int, start, end) -> int:
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == el:
            return mid
        elif arr[mid] > el:
            return recursive_binary_search(arr, el, start, mid-1)
        elif arr[mid] < el:
            return recursive_binary_search(arr, el, mid+1, end)
    else:
        return -1


a = [1, 4, 5, 8, 9, 25, 47]
print(recursive_binary_search(a, 10000, 0, len(a) - 1))
