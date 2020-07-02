#Problem ID: TSTROBOT
#Problem Name: Testing Robot

for _ in range(int(input())):
    n, x = map(int, input().split())
    l = [x]
    l = set(l)

    s = input()
    for i in range(n):
        if(s[i] == 'R'):
            x+=1
        else:
            x-=1
        l.add(x)
    print(len(l))

