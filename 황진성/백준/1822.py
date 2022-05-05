import sys


def input():
	return sys.stdin.readline().rstrip()


ignored = input()
s1 = set(input().split())
s2 = set(input().split())
res = list(map(int, s1 - s2))
print(len(res))
if len(res) > 0:
	print(' '.join(map(str, sorted(res))))