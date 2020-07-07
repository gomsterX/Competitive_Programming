#Problem ID: CHEALG
#Problem Name: Check Algorithm

for _ in range(int(input())):
    s = list(input())
    i = 0
    x = 0
    c = 1
    while i < len(s):

        if(i+1 == len(s) or s[i] != s[i+1]):
            x+=len(str(c))+1
            c = 1
        else:
            c+=1
        i+=1
    if(x < len(s)):
        print('YES')
    else:
        print('NO')
