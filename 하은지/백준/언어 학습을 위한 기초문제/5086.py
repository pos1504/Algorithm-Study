# [0] 약수 or 배수 판별 함수 정의
def distinction(A, B):
    if ((A == 0) & (B == 0)):
        return 0
    
    elif ((A % B) == 0):
        print("multiple")
        A, B = map(int, input().split())
        return distinction(A, B)
        
    
    elif ((B % A) == 0):
        print("factor")
        A, B = map(int, input().split())
        return distinction(A, B)

    else :
        print("neither")
        A, B = map(int, input().split())
        return distinction(A, B)

        
# [1] 함수 호출
A, B = map(int, input().split())
distinction(A, B)
