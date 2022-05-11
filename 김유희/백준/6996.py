import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A, B = input().split()

    Alist = list(A)
    Blist = list(B)

    if(sorted(Alist) == sorted(Blist)):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')
