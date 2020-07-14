#Problem ID: QUALPREL
#Problem Name: Qualifying to Pre-Elimination

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse = True)
    while True:
        if k == n or  l[k] != l[k-1]:
            break
        k+=1
    print(k)
