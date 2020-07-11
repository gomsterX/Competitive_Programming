#Problem ID: CACHEHIT
#Problem Name: Cache Hits

for _ in range(int(input())):
    n, b, m = map(int, input().split())
    l = list(map(int, input().split()))
    c = 1
    acc = l[0]//b
    for i in range(m):
        if l[i]//b != acc:
            c+=1
            acc = l[i]//b
    print(c)
