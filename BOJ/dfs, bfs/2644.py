import sys
from collections import deque


def bfs(node, end, field):
    visited = [0 for _ in range(n+1)]

    queue = deque()
    queue.append(node)
    count = 0
    while queue:
        node = queue.popleft()
        for n in field[node]:
            if not visited[n]:
                visited[n] = field[node] + 1
                queue.append(n)
        if node == end:
            break
        for i in range(n):
            if field[node][i] == 1:
                if not visited[node][i]:
                    visited[node][i] = 1
                    queue.append((node, i))
                    count += 1

    return count


n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())

field = [[0] * n for _ in range(n)]
for _ in range(int(sys.stdin.readline())):
    parent, child = map(int, sys.stdin.readline().split())
    field[parent-1][child-1] = field[child-1][parent-1] = 1
print(field)
print(bfs(start - 1, end - 1, field))