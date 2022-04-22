def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        immigration_count = 0
        for time in times:
            immigration_count += mid // time
        if immigration_count >= n:
            right = mid - 1
            answer = mid
        elif immigration_count < n:
            left = mid + 1

    return answer