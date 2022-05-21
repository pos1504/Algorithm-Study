# [0] 변수 선언부
word = input()
list = []
dic  = {}

# [1] 해당 알파벳을 find 후 딕셔너리에 인자값으로 바인딩
for i in range(ord('a'), ord('z')+1):
    num = word.count(chr(i)) + word.count(chr(i).upper())
    
    if(num <= 0):
        pass
    else:
        dic[chr(i).upper()] = num


# [2] 가장 많이 나온 알파벳을 대문자 형태로 하나 출력 -> 같을 경우 ? 처리
if(len(dic) == 1):
    for K, V in dic.items():
        print(K)
   
else:
    MAX = max(dic.values())

    for K, V in dic.items():
        if(V == MAX):
            list.append(K)

    if(len(list) > 1):
        print("?")
    elif(len(list) == 1):
        print("".join(list))
