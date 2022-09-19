def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        if len(s[i]) != 0:
            s[i] = s[i][0].upper() + s[i][1:].lower()
    return ' '.join(s)