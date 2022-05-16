import sys


def input():
	return sys.stdin.readline().rstrip()


def sum_nums(serial):
	sum = 0
	splited = list(serial)
	for sp in splited:
		if '0' <= sp <= '9':
			sum += int(sp)
	return sum


n = int(input())
serials = [input() for _ in range(n)]
print('\n'.join(sorted(serials, key=lambda s: (len(s), sum_nums(s), s))))
