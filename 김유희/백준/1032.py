import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline() for _ in range(n)]

for i in range(len(words[0])-1):
    result = words[0][i]
    for j in range(n):
        if result != words[j][i]:
            print('?', end='')
            break
    else:
        print(result, end='')
