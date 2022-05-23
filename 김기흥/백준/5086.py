A = []
B = []
while(True):
  a, b = map(int, input().split())
  if(a == 0 and b == 0):break
  A.append(a)
  B.append(b)

for i in range(len(A)):
  if B[i]%A[i] == 0 : print('factor')
  elif A[i]%B[i] == 0: print("multiple")
  else: print("neither")
