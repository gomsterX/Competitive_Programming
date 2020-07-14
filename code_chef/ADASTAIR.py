#Problem ID: ADASTAIR
#Problem Name: Ada and the Staircase

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    c = 0
    for i in range(1, n):
        m = l[i]-l[i-1]
        if m > k:
            c+= m//k
    print(c)


