import sys


def binary_search(low, high):
    target = high
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


n = int(sys.stdin.readline())
print(binary_search(0, n))

