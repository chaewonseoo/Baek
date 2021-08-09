import sys

if __name__ == '__main__':
    n, want = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))
    start, end = 1, max(trees)

    while start <= end:
        mid = (start + end) // 2

        total = 0   # 잘린 나무의 합
        for i in trees:
            if i >= mid:    # mid보다 높이가 크면 잘림
                total += i - mid
        if total >= want:   # 원하는 높이이거나 더 많이 잘렸으면
            start = mid + 1
        else:   # 원하는 높이보다 덜 잘렸으면
            end = mid - 1
    print(end)
