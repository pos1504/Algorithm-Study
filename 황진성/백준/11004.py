import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
print(sorted(list(map(int, input().split())))[k - 1])