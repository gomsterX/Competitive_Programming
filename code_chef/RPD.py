#Problem ID: RPD
#Problem Name: Easy Math

def sum_digits(x):
    c = 0
    for i in range(len(str(x))):
        c += x%10
        x//=10
    return c

for _ in range(int(input())):
    l = []
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        for j in range(i, n):
            if i != j:
                l.append(sum_digits(nums[i]*nums[j]))

    print(max(l))
