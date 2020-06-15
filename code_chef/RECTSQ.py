#Problem ID: RECTSQ
#Problem Name: Farmer And His Plot

import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    gcd = math.gcd(x,y)
    print(int((x/gcd)*(y/gcd)))
