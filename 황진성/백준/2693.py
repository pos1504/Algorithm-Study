import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
for _ in range(n):
	print(sorted(map(int, input().split()))[-3])