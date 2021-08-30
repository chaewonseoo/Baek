import sys
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        for i in graph[queue.popleft()]:
            if infection[i] == 0:
                queue.append(i)
                infection[i] = 1

if __name__ == '__main__':
    computer = int(sys.stdin.readline())
    connect = int(sys.stdin.readline())

    graph = [[] for i in range(computer + 1)]
    for i in range(connect):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    infection = [0] * (computer + 1)
    bfs(1)
    print(infection.count(1) - 1)
