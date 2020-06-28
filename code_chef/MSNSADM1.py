#Problem ID: MSNSADM1
#Problem Name: Football

for _ in range(int(input())):
    n = int(input())
    g = list(map(int, input().split()))
    f = list(map(int, input().split()))

    m = 0
    for i in range(n):
        m = max(m, g[i]*20 - f[i] *10)
    print(m)
