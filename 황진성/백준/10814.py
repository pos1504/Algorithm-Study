import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
data = []
for idx in range(n):
	inp = input().split()
	# join index, age, name
	data.append([idx, int(inp[0]), inp[-1]])

data.sort(key=lambda d: (d[1], d[0]))

for d in data:
	print(d[1], d[2])