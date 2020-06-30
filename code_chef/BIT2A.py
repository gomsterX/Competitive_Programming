#Problem ID: BIT2A
#Problem Name: A - Books

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    l=[]
    i=0
    while(i < n):
        x=1
        while(i+1 < n and nums[i] == nums[i+1]):
            i+=1
            x+=1
        l += [n-i-1]*x
        i+=1
    print(l)
