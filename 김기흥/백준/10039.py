A = []
for i in range(5):
  a = int(input())
  if a < 40:
    A.append(40)
  else:
    A.append(a)

print(int(sum(A)/len(A)))
