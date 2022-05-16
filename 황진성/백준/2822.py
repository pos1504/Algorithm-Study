import sys


def input():
	return sys.stdin.readline().rstrip()


data = []
for idx in range(8):
	data.append((int(idx) + 1, int(input())))

max_score_data = sorted(data, key= lambda d: -d[1])[:5]
print(sum([max_score_data[i][1] for i in range(5)]))
print(' '.join(map(str, sorted([max_score_data[i][0] for i in range(5)]))))