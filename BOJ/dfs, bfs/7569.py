import sys
from collections import deque


def bfs(tomato):
    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    dx = [0, 0, -1, 1, 0, 0]    # 열
    dy = [0, 0, 0, 0, -1, 1]    # 행
    dz = [1, -1, 0, 0, 0, 0]    # 높이

    cnt = 0
    tomato = deque(tomato)
    temp_tomato = deque()
    while tomato:
        z, y, x = tomato.popleft()  # z: 높이, y: 행, x: 열

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if box[nz][ny][nx] == 0:
                    temp_tomato.append((nz, ny, nx))
                    box[nz][ny][nx] = 1

        if not tomato:
            cnt += 1
            tomato.extend(temp_tomato)
            temp_tomato = deque()

    return is_all_ripe(cnt)


def is_all_ripe(cnt):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    cnt = 0
    return cnt - 1


m, n, h = map(int, sys.stdin.readline().split())
box = []
for _ in range(h):
    temp_box = []
    for _ in range(n):
        temp_box.append(list(map(int, sys.stdin.readline().split())))
    box.append(temp_box)

tomato = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                tomato.append((i, j, k))
print(bfs(tomato))