import sys

N = int(sys.stdin.readline())
birth = []

for _ in range(N):
    birth.append(list(map(str, sys.stdin.readline().strip().split())))
birth.sort(key = lambda x : (int(x[-1]), int(x[-2]), int(x[-3])))

print(birth[-1][0])
print(birth[0][0])
