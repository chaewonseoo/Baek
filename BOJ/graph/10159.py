import sys
INF = int(1e9)

N = int(sys.stdin.readline())
things = [[0] * N for _ in range(N)]
for _ in range(int(sys.stdin.readline())):
    thing1, thing2 = map(int, sys.stdin.readline().split())
    things[thing1-1][thing2-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if things[i][k] == 1 and things[k][j] == 1:
                things[i][j] = 1

answer = 0
for i in range(N):
    count = 0
    for j in range(N):
        count += things[i][j] + things[j][i]
    print((N - 1) - count)