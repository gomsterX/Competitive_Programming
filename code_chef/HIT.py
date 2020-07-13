#Problem ID: HIT
#Problem Name: Khaled in HIT

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l = sorted(l)
    x = n//4
    y = l[(2*x)]
    z = l[(3*x)]
    p = x
    x = l[x]
    if x==l[p-1] or y==l[((2*p)-1)] or z==l[((3*p)-1)]:
        print(-1)
    else:
        print(x,y,z)

