import sys

x, y = map(int, sys.stdin.readline().split())
score = (y * 100) // x

if score >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if (y + mid) * 100 // (x + mid) > score:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)