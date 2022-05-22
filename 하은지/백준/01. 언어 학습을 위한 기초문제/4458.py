# [0] 변수 선언부 
T   = int(input())
new = ''

# [1] 첫 글자 -> 대문자로 변환 후 출력 
for i in range(T):
    Sentence = input()

    new = Sentence[0].upper()
    print(new + Sentence[1:])      
