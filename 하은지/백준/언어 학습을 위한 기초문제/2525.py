# [0] time함수 생성 
def time (A, B):  
    if (A == 24):
      A = 0
    
    if (B < 60):
        return A, B

    else :
        B = B - 60
        A = A + 1 
        return time(A, B)

# [1] 변수 선언부
A, B = map(int, input().split())
C    = int(input())

# [2] 시각 계산
B = B + C
print("%d %d" % time(A, B))
