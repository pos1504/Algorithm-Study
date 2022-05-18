A, B = map(int,input().split())
C = int(input())
if(B+C >= 60):A += int((B+C)/60)
if A>=24:A %= 24
print(A, (B+C)%60)

