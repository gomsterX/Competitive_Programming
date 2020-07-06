#Problem ID: COUPSYS
#Problem Name: Coupon System

for _ in range(int(input())):
    n = int(input())
    l1, l2, l3 = [0, 0], [0, 0], [0, 0]
    for i in range(n):
        x = list(map(int, input().split()))
        if x[1] == 1:
            if x[2] > l1[0]:
                l1[0] = x[2]
                l1[1] = x[0]
            elif x[2] == l1[0] and x[0] < l1[1]:
                l1[1] = x[0]
        if x[1] == 2:
            if x[2] > l2[0]:
                l2[0] = x[2]
                l2[1] = x[0]
            elif x[2] == l2[0] and x[0] < l2[1]:
                l2[1] = x[0]
        if x[1] == 3:
            if x[2] > l3[0]:
                l3[0] = x[2]
                l3[1] = x[0]
            elif x[2] == l3[0] and x[0] < l3[1]:
                l3[1] = x[0]
    print(*l1, sep=' ')
    print(*l2, sep=' ')
    print(*l3, sep=' ')

