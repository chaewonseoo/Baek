import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    L = sorted(list(map(int, sys.stdin.readline().split())))
    result = 0
    for i in range(n - 2):
        result = max(result, abs(L[i] - L[i + 2]))
    print(result)
