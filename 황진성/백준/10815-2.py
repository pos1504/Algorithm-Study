import sys


def input():
	return sys.stdin.readline().rstrip()


ignored = input()
cards = set(map(int, input().split()))
ignored = input()
find = list(map(int, input().split()))

ans = ''
for f in find:
	# set은 해시 자료구조이므로 O(1)
	if f in cards:
		ans += '1 '
	else:
		ans += '0 '

print(ans)