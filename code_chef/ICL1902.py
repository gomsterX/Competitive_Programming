#Problem ID: ICL1902
#Problem Name: FlatLand

import math

for _ in range(int(input())):
    n = int(input())
    squares = 0

    c = 0
    while(n > 0):
        if(math.sqrt(n) % 1 != 0):
            n -= 1
            c += 1
        else:
            squares += 1
            n = c
            c = 0

    print(squares)
