import sys

n = int(sys.stdin.readline())
num = n // 5
while True:
    if num == 0 and n % 2 != 0:
        print(-1)
        break
    if (n - num * 5) % 2 != 0:
        num -= 1
    else:
        print(num + (n - num * 5) // 2)
        break
