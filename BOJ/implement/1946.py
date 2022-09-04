import sys

for _ in range(int(sys.stdin.readline())):
    N, cnt = int(sys.stdin.readline())
    rank = [list((map(int, sys.stdin.readline().split()))) for _ in range(N)]
    for i in rank:
        for j in rank:
            if i[0] > j[0] and i[1] > j[1]:
                cnt -= 1
                break
    print(cnt)
