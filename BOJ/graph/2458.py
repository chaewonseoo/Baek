from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
student = [([0] * N) for _ in range(N)]
for _ in range(M):
    small, tall = map(int, input().split())
    student[small-1][tall-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if student[i][k] == 1 and student[k][j] == 1:
                student[i][j] = 1
for i in range(N):
    print(student[i])

answer = 0
for i in range(N):
    check = 0
    for j in range(N):
        check += student[i][j] + student[j][i]
    if check == (N - 1):
        answer += 1
print(answer)
