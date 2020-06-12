#Problem ID: COPS
#Problem Name: Cops and the Thief Devu

for _ in range(int(input())):

    #Taking the inputs
    houses = [False] * 100
    x, y, z = map(int, input().split())
    max_check = y*z
    cops_houses = list(map(int, input().split()))

    #mark the checked houses
    for i in cops_houses:
        x1 = i - 1 - max_check
        x1 = x1 if (x1>0) else 0

        x2 = i + max_check
        x2 = x2 if (x2 < 100) else 100
        for j in range(x1, x2):
            houses[j] = True

    #to print the number of safe houses
    print(houses.count(False))

