import sys


def dfs(n):
    for i in graph[n]:
        if answer[i] == -1:
            answer[i] = n
            print(i, answer[i])
            dfs(i)


N = int(sys.stdin.readline())
graph = [[] for i in range(N + 1)]
answer = [-1] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
dfs(1)

# for i in range(2, N + 1):
#     print(answer[i])
