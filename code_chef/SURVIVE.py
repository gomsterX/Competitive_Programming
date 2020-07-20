#Problem ID: SURVIVE
#Problem Name: Survive in ChocoLand

import math

for _ in range(int(input())):
    n,k,s = map(int,input().split())
    x = (k*s)
    y = (s-(s//7))*n
    if x > y:
        print("-1")
    else:
        print( math.ceil(x/n) )
