# [0] 변수 선언 및 점수 입력
average = 0

for i in range(5):
    student = int(input())

    if student < 40:
       student = 40

    average += student

# [1] 평균 출력 
print(int(average//5))
