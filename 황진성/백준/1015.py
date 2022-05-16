import sys


def input():
	return sys.stdin.readline().rstrip()


ignored = input()

inp = list(map(int, input().split()))
data = [[v, p] for p, v in enumerate(inp)]

data.sort(key=lambda d: (d[0], d[1]))
for n, d in enumerate(data):
	d.append(n)

data.sort(key=lambda d: d[1])
for d in data:
	print(d[-1], end=' ')


"""
v : value
p : position
n : new_index

origin
v 2 1 3 1
p 0 1 2 3

sort (v, p)
v 1 1 2 3
p 1 3 0 2
n 0 1 2 3

sort (p)
v 
p 0 1 2 3
n 2 0 3 1
"""