import sys

wave_list = [0] * 101
wave_list[1], wave_list[2], wave_list[3] = 1, 1, 1

for i in range(98):
    wave_list[i + 3] = wave_list[i] + wave_list[i + 1]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(wave_list[n])