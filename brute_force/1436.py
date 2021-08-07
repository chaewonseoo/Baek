import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    i, cnt = 666, 0
    while True:
        if '666' in str(i):
            cnt += 1
            if cnt == n:
                print(i)
                break
        i += 1
