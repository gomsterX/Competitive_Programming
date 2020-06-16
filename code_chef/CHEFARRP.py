#Problem ID: CHEFARRP
#Problem Name: Chef and Subarrays

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        s = 0
        p = 1
        for j in range(i, n):
            s += a[j]
            p *= a[j]
            if(s == p):
                count += 1

    print(count)
