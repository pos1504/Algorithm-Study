import sys
input = sys.stdin.readline().strip() #input()

word = input.upper()
cnt = {}

for i in range(len(word)):
    if word[i] not in cnt:
        cnt[word[i]] = 1 #init
    elif word[i] in cnt:
        cnt[word[i]] += 1

maxNum = max(cnt.values())
result = []

for k,v in cnt.items():
    if v == maxNum:
        result.append(k)

if len(result) == 1:
    print(result[0])
elif len(result) != 1:
    print("?")

