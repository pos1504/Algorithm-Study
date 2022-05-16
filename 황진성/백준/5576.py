import sys


def input():
	return sys.stdin.readline().rstrip()


print(sum(sorted([int(input()) for _ in range(10)])[-3:]))
print(sum(sorted([int(input()) for _ in range(10)])[-3:]))
