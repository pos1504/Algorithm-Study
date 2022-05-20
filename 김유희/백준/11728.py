# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# NList = list(map(int, input().split()))
# MList = list(map(int, input().split()))
#
# NewList = NList + MList
# print(' '.join(map(str,sorted(NewList))))

import sys
N,M = sys.stdin.readline().split()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))
