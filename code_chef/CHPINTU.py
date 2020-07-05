#Problem ID: CHPINTU
#Problem Name: Pintu and Fruits

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    c = list(map(int, input().split()))

    x = set(l)
    t_cost = []
    for i in x:
        t = 0
        for j in range(n):
            if l[j] == i:
                t += c[j]
        t_cost.append(t)
    print(min(t_cost))
