txt = ''
while True:
    try:
        txt += input()             
    except:
        break
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
dic = {}
t_ls = []
tar = ''
idx = ''
for i in al:
    dic[i] = 0
for k in range(len(txt)):
    t_ls.append(txt[k])
for j in t_ls:
    if j == ' ':
        pass
    elif dic[j] == 0:
        dic[j] = 1
    else:
        dic[j] += 1
for n in al:
    if tar == '':
        tar += n
        idx = tar[0]
    elif dic[idx] == dic[n]:
        tar += n
        idx = tar[0]
    elif dic[idx] < dic[n]:
        tar = n
        idx = tar[0]
print(tar)
