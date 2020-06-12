#Problem ID: TRICOIN
#Problem Name: Coins And Triangle

import math

for _ in range(int(input())):
    sum_coins = int(input())

    #calculating the descriminant
    d = 1 + 4*2*sum_coins

    #calculating the minimum solution
    x1 = (-1+ math.sqrt(d))//2

    print(int(x1))

