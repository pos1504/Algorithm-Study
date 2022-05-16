import sys

N = int(sys.stdin.readline())
numbers = []

for i in str(N):
    numbers.append(i)

'''
버블 정렬
for i in range(N):
    for j in range(N):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
'''

numbers = sorted(numbers, reverse=True)
print("".join(map(str, numbers)))
