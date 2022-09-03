import sys

T = int(sys.stdin.readline())
A, B, C = 300, 60, 10

if T % C != 0:
    print(-1)
else:
    print(T // A, end=' ')
    T %= A
    print(T // B, end=' ')
    T %= B
    print(T // C, end=' ')
