from math import factorial

if __name__ == '__main__':
    n, k = map(int, input().split())
    res = factorial(n) // (factorial(k) * factorial(n - k))
    print(res)
