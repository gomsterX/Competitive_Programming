#Problem ID: DIET
#Problem Name: Chef Diet

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    p = 0
    d = -1
    for i in range(n):
        p += l[i]
        p-=k
        if p < 0:
            d = i
            break

    if d != -1:
        print("NO", i+1)
    else:
        print("YES")
