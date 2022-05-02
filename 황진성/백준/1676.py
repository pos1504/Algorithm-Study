n = int(input())

INT_MAX = 0x7fffffff
answer = 0

for i in range(1, INT_MAX):
	div = 5 ** i
	if n // div == 0:
		break
	answer += n // div

print(answer)
