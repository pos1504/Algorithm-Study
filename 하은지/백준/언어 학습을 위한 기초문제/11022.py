# [0] 변수 선언부
T = int(input())

# [1] 조건 및 출력
for i in range(T):
    A, B = map(int, input().split())

    print("Case #%d: %d + %d = %d" % (i+1, A, B, A+B))
