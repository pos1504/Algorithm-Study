from collections import Counter
import sys


def input():
	return sys.stdin.readline().rstrip()


books = Counter([input() for _ in range(int(input()))]).most_common()
print(sorted(books, key= lambda b: (-b[1], b[0]))[0][0])