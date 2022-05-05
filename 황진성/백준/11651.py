import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
data = []
for _ in range(n):
	data.append(tuple(map(int, input().split())))

data.sort(key=lambda d: (d[1], d[0]))

for d in data:
	print(d[0], d[1])