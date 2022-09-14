import sys
from bisect import bisect_left


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = sorted(list(map(int, sys.stdin.readline().split())))

    count = 0
    for number in a:
        count += bisect_left(b, number)
    print(count)