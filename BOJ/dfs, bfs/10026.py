import sys
sys.setrecursionlimit(1000000)

three_count, two_count = 0, 0
n = int(sys.stdin.readline())
section = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    visited[x][y] = True
    current_color = section[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                if current_color == section[nx][ny]:
                    dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            three_count += 1

for i in range(n):
    for j in range(n):
        if section[i][j] == 'R':
            section[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            two_count += 1

print(three_count, two_count)
