#Problem ID: POTATOES
#Problem Name: Farmer Feb

import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    x += y
    for i in range(x+1, 2100):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if(i % j == 0):
                is_prime = False
                j = int(math.sqrt(i))

        if(is_prime):
            print(i - x)
            break
