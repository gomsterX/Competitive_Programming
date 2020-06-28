#Problem ID: PLAYSTR
#Problem Name: Playing with Strings

for _ in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    c = 0
    for i in range(n):
        if(s[i] != r[i]):
            if(s[i] == '1'):
                c+=1
            else:
                c-=1
    if(not c):
        print("YES")
    else:
        print("NO")
