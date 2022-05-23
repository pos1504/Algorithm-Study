A = []
a, b, c = map(int,input().split())
A.append(a)
A.append(b)
A.append(c)


for i in range(len(A)):
  for k in range(len(A)):
    if A[i] < A[k]:
      tmp = A[i]
      A[i] = A[k]
      A[k] = tmp

print(A[1])
    
