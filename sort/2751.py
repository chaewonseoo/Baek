import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = []
    for _ in range(n):
        a.append(int(sys.stdin.readline()))
    for i in sorted(a):
        sys.stdout.write(str(i)+'\n')
