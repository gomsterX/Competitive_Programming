#Problem ID: ELEVSTRS
#Problem Name: From heaven to earth

import math

for _ in range(int(input())):
    n, v1, v2 = map(int, input().split())

    if(2*n/v2 < math.sqrt(2)*n/v1):
        print("Elevator")
    else:
        print("Stairs")
