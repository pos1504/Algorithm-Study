A = int(input())
B = input()
sum = 0
squared = 0
for i in range(len(B),0,-1):
  print(A*int(B[i-1]))
  sum += (A*int(B[i-1]))*(10**squared)
  squared += 1

print(sum)
