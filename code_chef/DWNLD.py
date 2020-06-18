#Problem ID: DWNLD
#Problem Name: Download file

for _ in range(int(input())):
    n, k = map(int, input().split())
    used_bytes = 0
    for i in range(n):
        t, d = map(int, input().split())
        if(t < k):
            k-=t
        else:
            t = t - k if k > 0 else t
            k = 0
            used_bytes += d*t
    print(used_bytes)

