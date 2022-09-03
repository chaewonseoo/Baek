import sys

h = int(sys.stdin.readline())
eight_num = h // 2
if h == 0:
    print(1)
elif h == 1:
    print(0)
else:
    if h % 2 != 0:
        print(4, end='')
    print('8' * eight_num)
