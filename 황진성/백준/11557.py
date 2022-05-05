import sys


def input():
	return sys.stdin.readline().rstrip()


tc = int(input())
while tc > 0:
	tc -= 1

	n = int(input())
	max_col = ('', 0)
	for _ in range(n):
		inp = input().split()
		col = inp[0]
		size = int(inp[1])

		if max_col[1] < size:
			max_col = (col, size)

	print(max_col[0])