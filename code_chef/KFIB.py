#Problem ID: KFIB
#Problem Name: K Fibonnaci

n,k=list(map(int,input().split()))
arr=[]
i=1
add=j=0
while i<=n:
    if i<=k:
        arr.append(1)
        add+=1
    else:
        arr.append(add)
        add+=add-arr[j]
        j+=1

    i+=1
print(arr[-1]%1000000007)
