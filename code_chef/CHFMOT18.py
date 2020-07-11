#Problem ID: CHFMOT18
#Problem Name: Chef and Demonetisation

for _ in range(int(input())):
    s, n = map(int, input().split())
    c = 0
    while s > 0:
        if s >=n:
            x = s//n
            c+=x
            s -= (x*n)
        else:
            if s%2==0 or s == 1:
                n = s
            else:
                n = s-1
    print(c)
