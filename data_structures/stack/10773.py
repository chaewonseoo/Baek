if __name__ == '__main__':
    stack = []
    for _ in range(int(input())):
        n = int(input())
        if n == 0:
            stack.pop()
        else:
            stack.append(n)

    print(sum(stack))
