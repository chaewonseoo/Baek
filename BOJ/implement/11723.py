import sys

if __name__ == '__main__':
    s = set()
    for _ in range(int(sys.stdin.readline())):
        operation = sys.stdin.readline().strip()
        if operation == 'all':
            s = {i for i in range(1, 21)}
        elif operation == 'empty':
            s = set()
        else:
            operation, x = operation.split()
            x = int(x)
            if operation == 'add':
                s.add(x)
            elif operation == 'remove':
                s.discard(x)
            elif operation == 'check':
                print(1 if x in s else 0)
            elif operation == 'toggle':
                if x in s:
                    s.remove(x)
                else:
                    s.add(x)
