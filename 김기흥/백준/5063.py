N = int(input())
A=[]
for i in range(N):
  r, e, c = map(int, input().split())
  A.append([r, e, c])
for i in range(N):
  if (A[i][1] - (A[i][0]+A[i][2]))<0:
    print("do not advertise")
  elif (A[i][1] - (A[i][0]+A[i][2]))==0:
    print("does not matter")
  else:
    print("advertise")
