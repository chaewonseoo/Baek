import sys


class queue():
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, x):
        self.queue.append(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.queue.pop(0)

    def my_size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.queue[-1]


if __name__ == '__main__':
    queue = queue()
    n = int(sys.stdin.readline())
    for _ in range(n):
        command = sys.stdin.readline().split()
        if command[0] == 'push':
            queue.push(command[1])
        elif command[0] == 'pop':
            sys.stdout.write(str(queue.pop()))
            sys.stdout.write("\n")
        elif command[0] == 'size':
            sys.stdout.write(str(queue.my_size()))
            sys.stdout.write("\n")
        elif command[0] == 'empty':
            sys.stdout.write(str(queue.empty()))
            sys.stdout.write("\n")
        elif command[0] == 'front':
            sys.stdout.write(str(queue.front()))
            sys.stdout.write("\n")
        elif command[0] == 'back':
            sys.stdout.write(str(queue.back()))
            sys.stdout.write("\n")
