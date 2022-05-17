# [0] 변수 선언부
A, B, C = map(int, input().split())

# [1] 연산 결과 출력
print("{}".format((A+B)%C))
print("{}".format(((A%C) + (B%C))%C))
print("{}".format((A*B)%C))
print("{}".format(((A%C) * (B%C))%C))
