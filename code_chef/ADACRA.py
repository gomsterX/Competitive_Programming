#Problem ID: ADACRA
#Problem Name: Ada and crayons

for _ in range(int(input())):
    s = input()
    u = s.count('DU')
    d = s.count('UD')

    if(s[0] == 'D'):
        d+=1
    else:
        u+=1
    if(s[len(s) - 1] == 'U'):
        u+=1
    else:
        d+=1
    print(d, u)
