import sys
import heapq

N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    queue.append([S, T])

queue.sort()
room = []
heapq.heappush(room, queue[0][1])
for i in range(1, N):
    if queue[i][0] < room[0]:
        heapq.heappush(room, queue[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, queue[i][1])

print(len(room))
