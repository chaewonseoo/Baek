import sys
from collections import deque


def dfs(node, node2):
    queue = deque()
    queue.append((node, 1))
    while queue:
        x, t = queue.popleft()
        if x > node2:
            continue
        if x == node2:
            print(t)
            break
        queue.append((x * 2, t + 1))
        queue.append((x * 10 + 1, t + 1))
    else:
        print(-1)


A, B = map(int, sys.stdin.readline().split())
dfs(A, B)
