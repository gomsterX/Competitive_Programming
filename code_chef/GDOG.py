#Problem ID: GDOG
#Problem Name: Greedy puppy

for _ in range(int(input())):
    coins, no_of_people = map(int, input().split())

    tuzik_coins = 0
    if (coins < no_of_people):
        tuzik_coins = coins
    for i in range(1, no_of_people + 1):
        if(coins % i > tuzik_coins):
            tuzik_coins = coins%i

    print(tuzik_coins)
