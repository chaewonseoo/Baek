import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
dp[1], dp[2] = 1, 2

if n <= 3: print(n)
else:
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[i] % 10007)
