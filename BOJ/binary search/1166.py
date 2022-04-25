import sys

n, l, w, h = map(int, sys.stdin.readline().split())
low, high = 0, min(l, w, h)
for _ in range(1000):
    mid = (low + high) / 2
    if (l // mid) * (w // mid) * (h // mid) >= n:
        low = mid
    else:
        high = mid
print("%.10f" %(high))