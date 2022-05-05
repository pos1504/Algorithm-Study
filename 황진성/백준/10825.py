import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
data = []
for _ in range(n):
	inp = input().split()
	stu = [inp[0]]
	stu.extend(map(int, inp[1:]))
	data.append(stu)

data.sort(key=lambda d: (-d[1], d[2], -d[3], d[0]))

for d in data:
	print(d[0])