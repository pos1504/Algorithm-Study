import sys
input = sys.stdin.readline

N = int(input())
ages = [input() for _ in range(N)]
ages.sort(key=lambda x: int(x.split()[0]))
print(''.join(ages))

"""
2)

import sys
input = sys.stdin.readline

N = int(input().strip())
ages = []

for _ in range(N):
    ages.append(list(map(str, input().strip().split())))

ages.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(ages[i][0], ages[i][1])
    
"""
