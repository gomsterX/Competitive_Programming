#Problem ID: CHRL4
#Problem Name: Chef and Way

n,k=map(int,input().split())
a=list(map(int,input().split()))
p =[[a[0],0]]
for j in range(1,n):
    x=j-k
    if(x>p[0][1]):
        p.pop(0)
    t=p[0][0]*a[j]
    while(len(p)!=0 and t<p[-1][0]):
        p.pop()
    p.append([t,j])
op=p[-1][0] % 1000000007
print(op)

