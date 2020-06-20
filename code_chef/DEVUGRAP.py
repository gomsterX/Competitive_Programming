#Problem ID: DEVUGRAP
#Problem Name: Devu and Grapes

for _ in range(int(input())):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))

    ops = 0
    for i in x:
        ops =ops + min(i%k, k - (i%k)) if i > k else ops + k-i

    print(ops)
