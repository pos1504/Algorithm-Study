T = int(input())
R=[]
S=[]
for i in range(T):
  r, s = input().split()
  R.append(int(r))
  S.append(s)

for i in range(len(R)):
  for j in range(len(S[i])):
    for k in range(R[i]):
      print(S[i][j], end = '')
  print()
