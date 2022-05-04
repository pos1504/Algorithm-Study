import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    schools, alcohol = "", 0
    for _ in range(int(input())):
        name, cnt = input().rstrip().split()
        cnt = int(cnt)
        if( cnt > alcohol ):
            alcohol = cnt
            schools = name
    print(schools)
