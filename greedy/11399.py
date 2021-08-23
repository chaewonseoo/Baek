import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    line = sorted(list(map(int, sys.stdin.readline().split())))

    temp, res = 0, 0
    for i in line:
        temp += i
        res += temp
    print(res)
