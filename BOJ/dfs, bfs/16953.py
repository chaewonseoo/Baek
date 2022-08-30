import sys
from collections import deque


def dfs(node, node2):
    global answer
    global flag
    queue = deque()
    queue.append(node)
    while queue:
        x = queue.popleft()
        if x == node2:
            flag = True
            print(answer)
            break
        x1 = x * 2
        x2 = x * 10 + 1
        answer += 1
        if x1 <= node2:
            dfs(x1, node2)
        if x2 <= node2:
            dfs(x2, node2)
    else:
        print(-1)

A, B = map(int, sys.stdin.readline().split())
answer = 1
dfs(A, B, answer)
