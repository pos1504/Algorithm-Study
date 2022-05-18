# [0] 변수 선언부 
N    = int(input())
user = input()
sum  = 0

# [1] 연산 및 출력 
for i in range(N):
    sum += int(user[i]) 

print(sum)
