import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    coin = [int(sys.stdin.readline()) for _ in range(n)]
    coin.reverse()

    res = 0
    while True:
        for i in coin:
            if k // i > 0:
                res += k // i
                k = k % i
        if k == 0:
            break
    print(res)

