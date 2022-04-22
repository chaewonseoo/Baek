import sys


def binary_search(low, high):
    target = high
    while True:
        mid = (low + high) // 2
        print(mid, mid ** 2)
        if (mid ** 2) == target:
            return mid
        if mid ** 2 > target:
            high = mid
        elif mid ** 2 < target:
            low = mid


n = int(sys.stdin.readline())
print(binary_search(1, n))