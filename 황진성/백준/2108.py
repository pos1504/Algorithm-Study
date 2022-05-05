import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


n = int(input())
data = []
for _ in range(n):
	data.append(int(input()))

data.sort()


def get_common():
	cnt_ls = collections.Counter(data).most_common()
	if len(cnt_ls) > 1 and cnt_ls[0][1] == cnt_ls[1][1]:
		return cnt_ls[1][0]
	return cnt_ls[0][0]


print(round(sum(data) / n))
print(data[n // 2])
print(get_common())
print(data[-1] - data[0])
