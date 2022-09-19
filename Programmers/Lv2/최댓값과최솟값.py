def solution(s):
    numbers = list(map(int, s.split()))
    return '%d %d' %(min(numbers), max(numbers))