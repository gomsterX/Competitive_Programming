#Problem ID: SUBINC
#Problem Name: Count Subarrays

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    subs = 0
    c = 0

    for i in range(n):
        if(i + 1 < n and nums[i] <= nums[i+1]):
            c +=1
        else:
            subs += ((c * (c+1)) /2)
            c = 0

    print(int(subs + n))
