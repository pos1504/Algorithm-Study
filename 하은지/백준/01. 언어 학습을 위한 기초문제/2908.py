# [1] 변수 선언부
(F_Answer, S_Answer) = map(str, input().split())

F_Answer = list(F_Answer)
S_Answer = list(S_Answer)

F_answer = ''
S_answer = ''

# [1] 값 뒤집은 후 새로운 변수에 바인딩
for i in reversed(F_Answer):
    F_answer += i
    
for j in reversed(S_Answer):
    S_answer += j

F_answer = int(F_answer.strip())
S_answer = int(S_answer.strip())

# [2] 비교 연산 후 출력 
if (F_answer > S_answer):
    print(F_answer)
    
else:
    print(S_answer)
