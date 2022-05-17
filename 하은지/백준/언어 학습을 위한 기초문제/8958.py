# [0] 변수 선언부 
T    = int(input())
list = []
sum  = 0


# [1] 테스트 케이스(T)만큼 값 입력 
for i in range(T):
    problem = input() 



# [2] 입력 받은 값 채점  
    for j in range(len(problem)):
        
        if (problem[j] == 'O'):
            list.append(problem[j])

       # (입력 받은 값을 차례로 읽는 중) X를 만나면, 그 전에 (채점)결과 합산을 구함.  
        else:
            for j in range(len(list)):
                sum += (j+1)

       # 리스트 초기화 
            list = []


   # [*] (예외처리) 마지막에 'X'를 만나지 못할 경우 
    for k in range(len(list)):
        sum += (k+1)
        list = []
        

# [3] 출력 및 초기화       
    print(sum)
    sum = 0
