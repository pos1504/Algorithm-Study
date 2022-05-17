import sys

N = int(sys.stdin.readline())
grades = []

for i in range(N):
    grades = list(map(int, sys.stdin.readline().split()))
    del grades[0]
    grades.sort()
    print(f'Class {i + 1}')
    gap = []
    for i in range(len(grades)-1):
        gap.append(grades[i+1] - grades[i])
    print(f'Max {max(grades)}, Min {min(grades)}, Largest gap {max(gap)}')
