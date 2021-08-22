import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    memo = {}
    for _ in range(n):
        site, pw = sys.stdin.readline().split()
        memo[site] = pw

    for _ in range(m):
        print(memo[sys.stdin.readline().strip()])
