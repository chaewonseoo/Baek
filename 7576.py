import sys

if __name__ == '__main__':
    m, n, h = map(int, sys.stdin.readline().split())
    tomato = []
    for _ in range(h):
        temp_tomato = []
        for __ in range(n):
            temp_tomato.append(list(map(int, sys.stdin.readline().split())))
        tomato.append(temp_tomato)
    print(tomato)
