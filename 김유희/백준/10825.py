import sys

N = int(sys.stdin.readline())
grade = []

for _ in range(N):
    grade.append(list(map(str, sys.stdin.readline().strip().split())))

grade.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in grade:
    print(i[0])
