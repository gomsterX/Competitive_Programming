#Problem ID: LOSTMAX
#Problem Name: Find the Maximum Value

for _ in range(int(input())):
    nums = list(map(int, input().split()))

    for i in range(len(nums)):
        if(nums[i] == len(nums) - 1):
            del(nums[i])
            break

    print(max(nums))
