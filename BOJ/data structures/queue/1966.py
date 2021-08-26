import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n, m = map(int, sys.stdin.readline().split())
        importance = list(map(int, sys.stdin.readline().split()))
        idx = list(range(len(importance)))
        idx[m] = 'target'
        print(idx)
        cnt = 0
        for __ in range(len(importance)):
            a = importance.index(max(importance))
            for j in range(a):
                importance.append(importance.pop(0))
                idx.append(idx.pop(0))
            cnt += 1

            if idx[0] == 'target':
                print(cnt)
                break
            else:
                importance.pop(0)
                idx.pop(0)
