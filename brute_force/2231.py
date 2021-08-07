import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(1, n+1):
        A = list(map(int, str(i)))
        res = i + sum(A)
        if res == n:
            print(i)
            break
        if i == n:
            print(0)
