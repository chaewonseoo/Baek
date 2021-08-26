import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    coordinate = list(map(int, sys.stdin.readline().split()))
    coordinate2 = sorted(list(set(coordinate)))

    dic = {}
    for i in range(len(coordinate2)):
        dic[coordinate2[i]] = i
    for i in coordinate:
        print(dic[i], end=' ')
