import sys


def input():
	return sys.stdin.readline().rstrip()


ignored = input()
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans1, ans2 = 0, 0
for x, y in zip(a, reversed(b)):
	ans1 += x * y
for x, y in zip(reversed(a), b):
	ans2 += x * y
print(min(ans1, ans2))

