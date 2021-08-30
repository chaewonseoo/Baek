import sys
from collections import deque

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        operations = sys.stdin.readline().strip()
        n = int(sys.stdin.readline())
        num = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
        if n == 0:
            num = []

        reverse = 0
        flag = True
        for operation in operations:
            if operation == 'R':
                reverse += 1
            elif operation == 'D':
                if num:
                    if reverse % 2 == 0:
                        num.popleft()
                    else:
                        num.pop()
                else:
                    flag = False
                    break
        if flag:
            if reverse % 2 == 0:
                print('[' + ','.join(num) + ']')
            else:
                num.reverse()
                print('[' + ','.join(num) + ']')
        else:
            print("error")
