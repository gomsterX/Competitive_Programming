#Problem ID: CANDY123
#Problem Name: Bear and Candies 123

import math
for _ in range(int(input())):
    y, x = map(int, input().split())
    y = int(math.sqrt(y))
    x = int((-1 + math.sqrt(1 + 4*x))//2)
    if(y > x):
        print("Limak")
    else:
        print("Bob")
