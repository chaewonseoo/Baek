import sys

if __name__ == '__main__':
    a = [0] * 5

    for i in range(5):
        a[i] = int(sys.stdin.readline())

        if a[i] < 40:
            a[i] = 40

    avg = sum(a) / 5
    print(int(avg))
    
