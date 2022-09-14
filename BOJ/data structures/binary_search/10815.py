import sys


def binary_search(low, high, cards, number):
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] == number:
            return 1
        elif cards[mid] > number:
            high = mid - 1
        else:
            low = mid + 1
    return 0


n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for number in numbers:
    print(binary_search(0, n-1, cards, number), end=' ')
