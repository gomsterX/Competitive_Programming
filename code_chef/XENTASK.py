#Problem ID: XENTASK
#Problem Name: Xenny and Alternating Tasks

for _ in range(int(input())):
    n = int(input())
    xen = list(map(int, input().split()))
    yan = list(map(int, input().split()))

    x, y = 0, 0
    for i in range(n):
        if(i%2 == 0):
            x += xen[i]
            y += yan[i]
        else:
            x += yan[i]
            y += xen[i]

    print(min(x, y))
