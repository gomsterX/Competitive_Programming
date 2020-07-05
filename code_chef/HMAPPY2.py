#Problem ID: HMAPPY2
#Problem Name: Appy and Contest

import math
for _ in range(int(input())):
    n, a, b, k = map(int, input().split())
    c = math.gcd(a,b)
    c = (a*b)//c
    c = n//c

    x = n//a + n//b -c -c
    if(x>=k):
        print("Win")
    else:
        print("Lose")
