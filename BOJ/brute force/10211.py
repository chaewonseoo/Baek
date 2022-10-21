import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    X = list(map(int, sys.stdin.readline().split()))
    arr = [0] * N
    arr[0] = X[0]
    for i in range(1, N):
        arr[i] = max(arr[i - 1] + X[i], X[i])
    print(max(arr))