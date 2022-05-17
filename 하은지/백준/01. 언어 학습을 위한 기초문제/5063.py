# [0] 테스트 케이스 입력
N = int(input())

# [1] 조건 및 출력
for i in range(N):
    r, e, c = map(int, input().split())
    profit = r + c 

    if profit > e :
        print("do not advertise")
    elif profit == e:
        print("does not matter")
    else :
        print("advertise")
