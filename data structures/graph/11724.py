import sys
from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    result = 0
    visited = [0] * (n + 1)
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(i)
            result += 1
    print(result)
