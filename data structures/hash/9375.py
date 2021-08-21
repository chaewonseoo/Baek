import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        closet = {}
        n = int(sys.stdin.readline())
        for __ in range(n):
            costume, kinds = map(str, sys.stdin.readline().split())
            # 의상의 종류 저장 X, 개수만 저장
            if kinds in closet.keys():
                closet[kinds] += 1
            else:
                closet[kinds] = 1

        res = 1
        for key in closet:
            res *= closet[key] + 1
        print(res - 1)
