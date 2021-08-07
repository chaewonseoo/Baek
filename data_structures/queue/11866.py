import sys


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    table = [i for i in range(1, n+1)]

    print('<', end='')
    turn = 0
    while len(table) > 1:
        turn += k
        if turn > len(table):
            turn %= len(table)
            if turn == 0:
                turn += len(table)
        turn -= 1
        print(table.pop(turn), end=', ')
    print(table.pop(), end='')
    print('>')
