# [0] 그릇 형태 입력 
bowl  = input()
sum   = 0

# [1] 그릇의 최종 높이 출력 
for i in range(len(bowl)):
    # 첫 번째 그릇 설정 
    if (i == 0):
        second = bowl[i]
        first  = second
        sum    += 10

    # 그릇 형태 비교 후 연산
    else:
        second = bowl[i]

        if (bowl[i] == first):
            sum += 5
        else:
            sum += 10

        first = second

print(sum)
