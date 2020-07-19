#Problem ID: DEPCHEF
#Problem Name: Deputy Chef

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    l = []

    for i in range(n):
        if i == 0:
            left = -1
        else:
            left = i-1
        if i == n-1:
            right = 0
        else:
            right = i+1
        if (d[i] > (a[left] + a[right])):
            l.append(d[i])
    if len(l) > 0:
        print(max(l))
    else:
        print(-1)
