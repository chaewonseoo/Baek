import sys

if __name__ == '__main__':
    n, want = map(int, sys.stdin.readline().split())
    lanlines = [int(sys.stdin.readline()) for _ in range(n)]
    start, end = 1, max(lanlines)

    while start <= end:
        mid = (start + end) // 2

        total = 0
        for i in lanlines:
            total += i // mid

        if total >= want:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
