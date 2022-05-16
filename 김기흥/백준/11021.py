T = int(input())
C = []
for i in range(T):
  A, B = map(int,input().split())
  C.append(A+B)
for i in range(T):
  print("Case #%d: %d" %(i+1,C[i]))

  
