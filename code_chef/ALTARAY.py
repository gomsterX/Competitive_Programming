#Problem ID: ALTARAY
#Problem Name: Alternating subarray prefix

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    subs = [1]
    for i in range(n-1, 0, -1):
        if(nums[i] * nums[i-1] < 0):
            subs.append(subs[(n-1) - i] + 1)
        else:
            subs.append(1)

    for i in reversed(subs):
        print(i, end = " ")
