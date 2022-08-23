from sys import stdin

input = stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)

route = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    route[start][end] = min(cost, route[start][end])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                route[i][j] = 0
            else:
                route[i][j] = min(route[i][j], route[i][k] + route[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if route[i][j] == INF:
            print("0", end=" ")
        else:
            print(route[i][j], end=" ")
    print()
