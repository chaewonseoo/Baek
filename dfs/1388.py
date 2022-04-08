import sys
from collections import deque


def solution(N, floor):
    visited = [[False] * M for _ in range(N)]

    def dfs(visited):
        queue = deque()
        for i in range(N):
            for j in range(M):
                queue.append([i, j])

        count = 0
        while queue:
            x, y = queue.popleft()
            if visited[x][y]:
                continue
            else:
                visited[x][y] = True

                if floor[x][y] == '-':
                    if y + 1 >= M:
                        count += 1
                        continue

                    if floor[x][y + 1] == '-':
                        continue
                    else:
                        count += 1
                        continue
                elif floor[x][y] == '|':
                    if x + 1 >= N:
                        count += 1
                        continue

                    if floor[x + 1][y] == '|':
                        if y + 1 >= M:
                            continue
                        queue.appendleft([x + 1, y])
                    else:
                        count += 1
                        continue
        return count
    return dfs(visited)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    floor = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(solution(N, floor))