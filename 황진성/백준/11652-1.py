import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
data = []
for _ in range(n):
	data.append(int(input()))

print(sorted(collections.Counter(data).most_common(), key=lambda tp: (-tp[1], tp[0]))[0][0])
