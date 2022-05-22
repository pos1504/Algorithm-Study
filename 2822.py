# import sys
# input = sys.stdin.readline
#
# scores = {}
#
# for i in range(8):
#     scores[i+1] = input().strip()
#
# scores = list(sorted(scores.items(), key = lambda x : -int(x[1])))
#
# sum = 0
# rank = []
# for i in range(5):
#     sum += int(scores[i][1])
#     rank.append(scores[i][0])
#     if(i == 4):
#         print(sum)
#
# print(' '.join(list(map(str, sorted(rank, key = int)))))

import sys

scores = list(map(int, sys.stdin.read().split()))
rank = sorted(scores)
print(sum(rank[3:]))
print(*sorted([scores.index(i)+1 for i in rank[3:]]))
