#Problem ID: PRICECON
#Problem Name: Chef and Price Control

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    los = 0
    for i in l:
        if i > k:
            los += i-k
    print(los)
