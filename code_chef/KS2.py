#Problem ID: KS2
#Problem Name: Guddu on a Date

for _ in range(int(input())):
    n = int(input())
    s=str(n)
    p=sum(map(int,s))
    if p%10==0:
        s=s+'0'
    else:
        s=s+str((10-(p%10)))
    print(s)
