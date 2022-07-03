import sys

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global house_count
        house_count += 1
        graph[x][y] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline()[:-1])))

house_list = []
house_count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            house_list.append(house_count)
            house_count = 0

house_list.sort()
print(len(house_list))
for cnt in house_list:
    print(cnt)
