if __name__ == '__main__':
    n = input()
    while n != '0':
        if n[::-1] == n:
            print("yes")
        else:
            print("no")
        n = input()
