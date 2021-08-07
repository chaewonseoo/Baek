import sys
from collections import deque

if __name__ == '__main__':
    queue = deque()
    for i in range(1, int(sys.stdin.readline())+1):
        queue.append(i)

    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue.pop())
