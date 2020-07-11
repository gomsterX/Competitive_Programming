#Problem ID: CHEFCHR
#Problem Name: Chef And His Characters

for _ in range(int(input())):
    s = input()
    m = []
    x = []
    c = 0
    for i in range(len(s)):
        if s[i] in 'chef':
            x.append(s[i])
        if s[i] not in 'chef' or i == len(s)-1 :
            if len(set(x))>=4:
                m.append(x)
            x = []
    for i in m:
        for j in range(len(i)-3):
            if(sorted(i[j:j+4])==sorted('chef')):
                c+=1
    if c:
        print('lovely', c)
    else:
        print('normal')
