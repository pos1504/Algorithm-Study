# [0] 변수 선언부 
word = input()
  # 정방향으로 읽은 단어를 저장하기 위한 리스트 
Forward_word   = []
  # 역방향으로 읽은 단어를 저장하기 위한 리스트 
Backward_word  = []


# [1] 리스트 & 값 바인딩  
for i in range(len(word)):
    Forward_word.append(word[i])

for i in range(len(word)-1, -1, -1):
    Backward_word.append(word[i])

 
# [2] 정방향으로 읽은 단어와 역방향으로 읽은 단어 비교 후 출력
if (Forward_word == Backward_word):
    print(1)    # 팰린드롬
    
else:
    print(0)    # 팰린드롬 X
