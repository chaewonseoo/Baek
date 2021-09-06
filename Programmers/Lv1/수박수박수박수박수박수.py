def solution(n):
    res = ''
    for i in range(n // 2):
        res += "수박"
    if n % 2 == 1:
        res += "수"

    return res