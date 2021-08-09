import sys

if __name__ == '__main__':
    num = sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])

    average = round(sum(num) / len(num))    # 산술평균
    median = num[(len(num) // 2)]   # 중앙값

    num_cnt = {}    # key: 입력받은 숫자, value: 숫자 당 빈도수
    for i in num:
        try:
            num_cnt[i] += 1
        except:
            num_cnt[i] = 1
    mode_num = max(list(num_cnt.values()))  # 딕셔너리의 value만 모아 리스트로 만든 후 그 중 최대값

    mode = []
    for i in num_cnt:
        if num_cnt.get(i) == mode_num:
            mode.append(i)


    # 출력
    print(average, median, sep='\n')
    if len(mode) < 2:
        print(mode[0])
    else:
        print(mode[1])
    print(abs(num[-1]-num[0]))
    
