import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    field[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == 1:
            dfs(nx, ny)


def solution(w, h, field):
    count = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i, j)
                count += 1
    return count


if __name__ == "__main__":
    while True:
        W, H = map(int, sys.stdin.readline().split())
        if W == 0 and H == 0:
            break
        field = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
        print(solution(W, H, field))