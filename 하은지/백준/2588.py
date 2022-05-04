# [0] 변수 선언부
A = int(input())
B = input()
C = list()

# [1] 연산 결과 -> 빈 리스트 C에 저장 
for i in B:
    C.append(A * int(i))

# [2] 출력 
for i in reversed(C):
    print(i)
    
print(A * int(B))
