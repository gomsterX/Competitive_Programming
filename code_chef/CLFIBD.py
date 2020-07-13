#Problem ID: CLFIBD
#Problem Name: Fibonacci String

for _ in range(int(input())):
    s = sorted(input())
    c = [s.count(s[0])]
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            c.append(s.count(s[i+1]))
    c.sort()

    dn = True
    if len(c)>2:
        if c[-1] != c[-2] + c[-3]:
            dn = False
    if dn:
        print('Dynamic')
    else:
        print('Not')
