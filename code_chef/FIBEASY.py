#Problem ID: FIBEASY
#Problem Name: Easy Fibonacci

for _ in range(int(input())):
    l=[]
    a=int(input())
    b=0
    c=1
    for j in range(0,60):
        if(j==0):
            l.append(0)
        elif(j==1):
            l.append(1)
        else:
            d=b+c
            b=c
            c=d
            l.append(c)
    l=[j%10 for j in l]
    m=1
    while(m*2<=a):
        m=m*2
    m=m%60
    print(l[m-1])
