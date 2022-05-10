# [0] 변수 선언부
T    = int(input())
list = []


# [1] 테스트 케이스(T)에 따라 값 입력 후 조정
for i in range(T):
    Test = input()
    
    if len(Test.split()) == 1:
        pass
    else:
        R, S = Test.split()
        R    = int(R)
        
        for i in S:
            for _ in range(R):
                list.append(i)


# [2] 출력
    if (len(list) == 0):
        pass
    else:
        P = ("".join(list)).strip()
        list = []
        
        print(P)
