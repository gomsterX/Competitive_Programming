#Problem ID: TWONMS
#Problem Name: Two Numbers

import math

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if(x > 0 and y > 0 and z > 0):
        x = x*2 if z % 2 != 0 else x
        print(max(x, y)//min(x, y))
