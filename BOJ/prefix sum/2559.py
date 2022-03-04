import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    temperatures = list(map(int, sys.stdin.readline().split()))

    for i in range(k-1):
        temperatures_add = [0]
        for j in range(n):
            temperatures_add.append(temperatures_add[-1]+temperatures[j])
        temperatures = temperatures_add
    print(temperatures)