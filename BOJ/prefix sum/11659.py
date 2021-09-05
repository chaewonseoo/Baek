import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums_add = [0]

    for i in range(n):
        nums_add.append(nums_add[-1]+nums[i])

    for _ in range(m):
        start, end = map(int, sys.stdin.readline().split())
        if i == 1:
            print(nums_add[end])
        else:
            print(nums_add[end] - nums_add[start - 1])
