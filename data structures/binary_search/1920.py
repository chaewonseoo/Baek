def binary_search(i, a, left, right):
    if left > right:
        return 0
    mid = (left + right) // 2
    if a[mid] > i:
        return binary_search(i, a, left, mid-1)
    elif a[mid] < i:
        return binary_search(i, a, mid+1, right)
    else:
        return 1


if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = int(input())
    b = list(map(int, input().split()))

    for i in b:
        left = 0
        right = n - 1
        print(binary_search(i, a, left, right))
