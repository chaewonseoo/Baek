import sys

S = list(sys.stdin.readline()[:-1])

zero_count, one_count = 0, 0
if S[0] == '0':
    zero_count += 1
else:
    one_count += 1

for i in range(1, len(S)):
    if S[i-1] != S[i]:
        if S[i] == '0':
            zero_count += 1
        else:
            one_count += 1
print(min(zero_count, one_count))
