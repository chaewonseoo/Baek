import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    coordinate = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    coordinate.sort(key=lambda x: (x[0], x[1]))
    for i in coordinate:
        print(i[0], i[1])
