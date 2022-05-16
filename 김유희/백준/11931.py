import sys

N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

'''
버블 정렬 사용
for i in range(N):
    for j in range(N):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
'''

numbers = sorted(numbers, reverse=True)
print("\n".join(map(str, numbers)))
