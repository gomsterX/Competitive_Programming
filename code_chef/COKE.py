#Problem ID: COKE
#Problem Name: Chef Drinks Coke

for _ in range(int(input())):
    n, m, k, l, r = map(int, input().split())
    can = None
    p = 1000010
    for i in range(n):
        x, y = map(int, input().split())
        if x > k:
            x = max(x-m, k)
        elif x < k:
            x = min(x+m, k)

        if x >=l and x <= r:
            if y < p:
                p = y
    if p != 1000010:
        print(p)
    else:
        print(-1)
