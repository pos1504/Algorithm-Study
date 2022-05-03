num = int(input())
txt = ''
le = 0
for i in range(num):
    txt += input()
    if i == 0:
        le = len(txt)
tar_ls = [True] * le
for k in range(le):
    for j in range(1,num):
        x = k + le * (j-1)
        y = k + le * j
        if txt[x] == txt[y]:
            tar_ls[k] = True
        else:
            tar_ls[k] = False
            break
result = ''
for n, q in zip(range(len(tar_ls)),tar_ls):
    if q:
        result += txt[n]
    else:
        result += '?'
print(result)
