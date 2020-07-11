#Problem ID: RECNDSTR
#Problem Name: Chef and String

for _ in range(int(input())):
    s = input()
    if(s[-1]+s[:-1] == s[1:]+s[0]):
        print('YES')
    else:
        print('NO')
