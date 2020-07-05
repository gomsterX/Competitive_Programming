#Problem ID: COVIDLQ
#Problem Name: COVID Pandemic and Long Queue

for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    z = 5
    i = 0
    r = True
    while i < n:
        if(s[i] == '1'):
            if(z<5):
                r = False
                break
            else:
                z = 0
        else:
            z+=1
        i += 1
    if(r):
        print('YES')
    else:
        print('NO')
