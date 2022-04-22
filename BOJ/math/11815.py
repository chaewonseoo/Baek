import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for number in numbers:
    if number == int(number ** 0.5) ** 2:
        print(1, end=" ")
    else:
        print(0, end=" ")