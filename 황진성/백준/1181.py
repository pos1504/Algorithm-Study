import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
s = set()
for _ in range(n):
	s.add(input())

data = list(s)
data.sort(key=lambda d: (len(d), d))

for d in data:
	print(d)
