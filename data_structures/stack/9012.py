if __name__ == '__main__':
    for _ in range(int(input())):
        s = list(input())
        stack = []
        flag = False

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if not stack:
                    flag = True
                    break
                else:
                    stack.pop()
        if not stack and not flag:
            print("YES")
        else:
            print("NO")
