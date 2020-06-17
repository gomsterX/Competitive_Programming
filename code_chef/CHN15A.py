#Problem ID: CHN15A
#Problem Name: Mutated Minions

for _ in range(int(input())):
    x, y = map(int, input().split())
    ls = list(map(int, input().split()))

    wolv = 0
    for i in ls:
        if((i+y) % 7 == 0):
            wolv += 1
    print(wolv)
