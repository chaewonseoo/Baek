import sys

if __name__ == '__main__':
    check = [0] * 10001
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        check[n] += 1

    for i in range(10001):
        if check[i] != 0:
            for _ in range(check[i]):
                print(i)
