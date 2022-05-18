T = int(input())
C = []
for i in range(T):
  A,B = map(int, input().split())
  C.append([A,B,A+B])
for i in range(T):
  print("Case #%d: %d + %d = %d" %(i+1,C[i][0],C[i][1],C[i][2]))
