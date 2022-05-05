import sys


def input():
	return sys.stdin.readline().rstrip()


ignored = input()
cards = sorted(list(map(int, input().split())))
ignored = input()
find = list(map(int, input().split()))


def bin_search(f):
	L, R = 0, len(cards) - 1
	while L <= R:
		mid = (L + R) // 2
		if cards[mid] < f:
			L = mid + 1
		elif cards[mid] > f:
			R = mid - 1
		elif cards[mid] == f:
			return 1
	return 0


for f in find:
	print(bin_search(f), end=' ')
