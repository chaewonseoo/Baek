import sys

fibo = [0, 1]
for i in range(2, 47):
    fibo.append(fibo[i-1] + fibo[i-2])

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    result = []
    while n:
        for k in range(46, 1, -1):
            if fibo[k] <= n:
                number = fibo[k]
                n -= number
                result.append(number)
                break

    result.sort()
    for i in result:
        print(i, end=' ')
    print()
