import sys

N = int(sys.stdin.readline())
stores = list(map(int, sys.stdin.readline().split()))
cnt = 0
for store in stores:
    if store == (cnt % 3):
        cnt += 1
print(cnt)
