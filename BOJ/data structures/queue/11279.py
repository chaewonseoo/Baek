import sys
import heapq

if __name__ == '__main__':
    heap = []
    for _ in range(int(sys.stdin.readline())):
        x = int(sys.stdin.readline())
        if x == 0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (-x, x))
