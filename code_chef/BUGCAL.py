#Problem ID: BUGCAL
#Problem Name: Buggy Calculator

for _ in range(int(input())):
    a, b = map(int, input().split())
    x, y = 0, 0

    while a or b:
        x += ((a%10 + b%10)%10) * (10**y)
        y+=1
        a//=10
        b//=10

    print(x)

