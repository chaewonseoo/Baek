import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    ans = 0
    cnt = 0
    i = 1
    while i < m - 1:
        if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
            cnt += 1
            if cnt == n:
                cnt -= 1    # 1
                ans += 1
            i += 1  # 2
        else:
            cnt = 0
        i += 1

    print(ans)
