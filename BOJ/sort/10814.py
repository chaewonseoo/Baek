if __name__ == '__main__':
    members = []
    for _ in range(int(input())):
        members.append(list(input().split()))
    members.sort(key=lambda x: int(x[0]))

    for i in range(len(members)):
        print(members[i][0], members[i][1])
