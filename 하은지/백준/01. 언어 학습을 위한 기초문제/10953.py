# [0] 변수 선언부 
T = int(input())

# [1] 연산 및 출력
for i in range(T):
    A, B   = map(int, input().split(','))
    print(A + B)
