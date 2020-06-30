#Problem ID: FBMT
#Problem Name: Football Match

for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        l.append(s)

    l.sort()
    x, y = 0, 0
    for i in l:
        if i == l[0]:
            x+=1
        else:
            y+=1
    if x>y:
        print(l[0])
    elif x<y:
        print(l[-1])
    else:
        print('Draw')
