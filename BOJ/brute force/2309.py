import sys

men = [int(sys.stdin.readline()) for _ in range(9)]
flag = False
for i in range(9):
    for j in range(i + 1, 9):
        if sum(men) - (men[i] + men[j]) == 100:
            men[i], men[j] = 0, 0
            break
    if flag:
        break

men = sorted(men)
del men[0]
del men[0]
[print(i) for i in men]
