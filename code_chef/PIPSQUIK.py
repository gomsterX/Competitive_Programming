#Problem ID: PIPSQUIK
#Problem Name: Full Barrier Alchemist

for _ in range(int(input())):
    n, h, y1, y2, l = map(int, input().split())
    b = 0
    p = True
    for i in range(n):
        t, x = map(int, input().split())
        if t == 1 and p:
            if (h-y1) <= x:
                b+=1
            elif l-1 > 0:
                l-=1
                b+=1
            else:
                p = False
        elif t == 2 and p:
            if y2 >= x:
                b+=1
            elif l-1 > 0:
                l-=1
                b+=1
            else:
                p = False
    print(b)
