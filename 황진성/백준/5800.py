import sys


def input():
	return sys.stdin.readline().rstrip()


class_size = int(input())

for class_idx in range(class_size):
	print(f'Class {class_idx + 1}')
	inp = list(map(int, input().split()))
	stu_size = inp[0]
	scores = sorted(inp[1:], reverse=True)

	largest_gap = 0
	curr_score = scores[0]
	for next_score in scores[1:]:
		curr_gap = curr_score - next_score
		curr_score = next_score
		if largest_gap < curr_gap:
			largest_gap = curr_gap

	print(f'Max {scores[0]}, Min {scores[-1]}, Largest gap {largest_gap}')
