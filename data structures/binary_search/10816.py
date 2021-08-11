import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    N = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    M = map(int, sys.stdin.readline().split())

    hashmap = {}
    for i in N:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    print(' '.join(str(hashmap[x]) if x in hashmap else '0' for x in M))
