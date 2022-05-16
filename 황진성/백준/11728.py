import sys


def input():
	return sys.stdin.readline().rstrip()


ignored = input()
data = []
data.extend(map(int, input().split()))
data.extend(map(int, input().split()))
print(' '.join(map(str, sorted(data))))