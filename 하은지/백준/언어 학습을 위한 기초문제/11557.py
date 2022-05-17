# [0] 변수 선언부 
T = int(input())
S_list = []
L_list = []

# [1] 술 소비가 가장 많은 학교의 이름 출력
for i in range(T):
    N = int(input())
    
    for j in range(N):
        S, L = map(str, input().split())

        S_list.append(S)
        L_list.append(int(L))

    Index = L_list.index(max(L_list))
    print(S_list[Index])
