#Problem ID: RD19
#Problem Name: Minimum Deletions

from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    g = gcd(l[0], l[1])
    for i in l:
        g = gcd(g, i)
    if g == 1:
        print(0)
    else:
        print(-1)
