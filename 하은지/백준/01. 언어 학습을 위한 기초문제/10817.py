# [1] 변수 선언부
A, B, C = map(int, input().split())
list    = []

# [2] 비교 연산 후 두 번째로 큰 정수 출력
if A > B:
    if A > C:
        if C > B:
            print(C)
        elif C < B:
            print(B)
        else:
            print(C)
    else:
        print(A)
        
elif A < B:
    if A < C:
        if C < B:
            print(C)
        elif C > B:
            print(B)
        else:
            print(C)
    else:
        print(A)

elif A == B:
    if B < C :
        print(B)
    elif A == B & B == C:
        print(A)
    else:
        print(B)

elif B == C:
    if A < C :
        print(A)
    elif A == B & B == C:
        print(A)
    else:
        print(A)

elif A == C:
    if A < C :
        print(A)
    elif A == B & B == C:
        print(A)
    else:
        print(A)
