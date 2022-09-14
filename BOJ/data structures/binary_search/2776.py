import sys


def binary_search(low, high, note1, number):
    while low <= high:
        mid = (low + high) // 2
        if note1[mid] == number:
            return 1
        elif note1[mid] > number:
            high = mid - 1
        else:
            low = mid + 1
    return 0


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    note1 = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))

    for number in note2:
        print(binary_search(0, n-1, note1, number))