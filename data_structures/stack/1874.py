import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    sequence = [int(sys.stdin.readline()) for _ in range(n)]

    stack = []
    result = []
    next_turn = 1
    flag = True
    for i in range(n):
        # 스택에 아무 값도 없을 때 혹은
        # 스택 마지막 값이 현재 pop 되어야 할 값보다 작을 때
        if len(stack) == 0 or stack[-1] < sequence[i]:
            for j in range(next_turn, sequence[i] + 1):
                stack.append(j)
                result.append("+")
            next_turn = sequence[i] + 1
        # 스택 마지막 값이 현재 pop 되어야 할 값보다 클 때
        elif stack[-1] > sequence[i]:
            flag = False
            break

        # 스택 마지막 값 == 현재 pop 되어야 할 값
        if stack[-1] == sequence[i]:
            stack.pop()
            result.append("-")

    if flag:
        print("\n".join(result))
    else:
        print("NO")
