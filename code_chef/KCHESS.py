#Problem ID: KCHESS
#Problem Name: Knight Chess

for _ in range(int(input())):
    n = int(input())
    knights = []
    for i in range(n):
        a, b = map(int, input().split())
        for i in range(-2, 3):
            if i == 0:
                continue
            y = 1 if i == -2 or i == 2 else 2
            knights.append(tuple([a+i, b+y]))
            knights.append(tuple([a+i, b-y]))

    a, b = map(int, input().split())
    king = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            king.append(tuple([a+i, b+j]))

    x = 0
    for i in knights:
        y, z = i
        if y == a and z == b:
            x -= 1
            break

    x += len(set(king).intersection(set(knights)))
    if x == 8:
        print('YES')
    else:
        print('NO')
