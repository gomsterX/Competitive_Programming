#Problem ID: CMPRSS
#Problem Name: Compress the List

for _ in range(int(input())):
    x=int(input())
    l=list(map(int,input().split()))
    count=""
    out = []
    j=0
    for i in range(len(l)-1):
        if l[i]+1!=l[i+1]:
            a=l[j:i+1]
            j=i+1
            out.append(a)
    else:
        a=l[j:]
        out.append(a)
    for i in out:
        a=i
        if len(a)>=3:
            count+=str(a[0])+"..."+str(a[len(a)-1])+","
        else:
            for j in range(len(a)):
                count+=str(a[j])+","
    print(count[:len(count)-1])

