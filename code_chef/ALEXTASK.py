#Problem ID: ALEXTASK
#Problem Name: Task for Alexey

from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    frz = max(l)*max(l)
    for i in range(n):
        for j in range(i+1, n):
            frz = min(frz, (l[i]*l[j])//gcd(l[i], l[j]))
    print(frz)
