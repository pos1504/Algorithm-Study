# [0] 변수 선언부
H, M = map(int, input().split())

# [1] 시간 계산 및 출력
if (44 < M < 60):
    M = M - 45
    
else:
    M = 60 + (M - 45)
    
    if (H <= 0):
        H = 23 - H
    else:
        H -= 1

print(H, M)
