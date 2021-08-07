import sys


if __name__ == '__main__':
    record = {
        'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0
    }
    n = int(sys.stdin.readline())
    gpa = 0.0
    total_credit = 0
    for _ in range(n):
        subject, credit, grade = sys.stdin.readline().split()
        gpa += int(credit) * record[grade]
        total_credit += int(credit)
    print("%.2f" % round(gpa/total_credit + 10**-10, 2))
