import sys

N, M = map(int, sys.stdin.readline().split())
if N > 0:
    books = list(map(int, sys.stdin.readline().split()))
    current_weight, cnt = 0, 1
    for book in books:
        if current_weight + book <= M:
            current_weight += book
        else:
            current_weight = book
            cnt += 1
    print(cnt)
else:
    print(0)
