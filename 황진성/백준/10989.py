import sys

MAX = 10_001


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
counting = [0] * MAX
for _ in range(n):
    counting[int(input())] += 1

for idx, c in enumerate(counting):
    while c > 0:
        c -= 1
        print(idx)