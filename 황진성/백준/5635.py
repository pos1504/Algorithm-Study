import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
data = []
for _ in range(n):
	inp = input().split()
	d = [inp[0]]
	d.extend(list(map(int, inp[1:])))
	data.append(d)

data.sort(key=lambda d: (d[-1], d[-2], d[-3]))

print(data[-1][0])
print(data[0][0])
