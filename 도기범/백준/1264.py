al = ['a', 'e', 'i', 'o', 'u']
n = 0
while True:
    n = 0
    ls = []
    txt = input().lower()
    if txt == '#':
        break 
    for i in range(len(txt)):
        if txt[i] in al:
            n += 1
        else:
            pass
    print(n)
