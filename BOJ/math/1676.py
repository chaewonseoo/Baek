import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    cnt = 0
    while n >= 5:
        cnt += n // 5
        n //= 5
        print(cnt, n)
    print(cnt)