#Problem ID: ISHVALA
#Problem Name: The Promised Land

for _ in range(int(input())):
    n,m=map(int,input().split())
    x,y,s=map(int,input().split())
    a=[]
    b=[]
    if x>0:
        a=list(map(int,input().split()))
    if y>0:
        b=list(map(int,input().split()))
    a=[0]+a[:]+[n+1]
    b=[0]+b[:]+[m+1]
    c=[]
    d=[]
    for i in range(len(a)-1):
        f=a[i+1]-a[i]
        if f>s:
            c.append((f-1)//s)
    for k in range(len(b)-1):
        g=b[k+1]-b[k]
        if g>s:
            d.append((g-1)//s)
    sum=0
    for l in c:
        sum+=l
    su=0
    for u in d:
        su+=sum*u
    print(su)
