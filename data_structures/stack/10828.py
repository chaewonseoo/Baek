import sys


class stack():
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.stack.pop()

    def my_size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size == 0:
            return -1
        else:
            return self.stack[-1]


if __name__ == '__main__':
    stack = stack()
    n = int(sys.stdin.readline())
    for _ in range(n):
        command = sys.stdin.readline().split()
        if command[0] == 'push':
            stack.push(command[1])
        elif command[0] == 'pop':
            sys.stdout.write(str(stack.pop()))
            sys.stdout.write("\n")
        elif command[0] == 'size':
            sys.stdout.write(str(stack.my_size()))
            sys.stdout.write("\n")
        elif command[0] == 'empty':
            sys.stdout.write(str(stack.empty()))
            sys.stdout.write("\n")
        elif command[0] == 'top':
            sys.stdout.write(str(stack.top()))
            sys.stdout.write("\n")
