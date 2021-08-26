import sys


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    card = sorted(list(map(int, sys.stdin.readline().split())))

    res = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if card[i] + card[j] + card[k] > m:
                    continue
                else:
                    res = max(res, card[i] + card[j] + card[k])
    print(res)
