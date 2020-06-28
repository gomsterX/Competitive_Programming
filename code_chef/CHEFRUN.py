#Problem ID: CHEFRUN
#Problem Name: Secret Recipe

for _ in range(int(input())):
    x, z, y, v1, v2= map(int, input().split())
    x = abs(x-y)/v1
    z = abs(y-z)/v2

    if x < z:
        print("Chef")
    elif x > z:
        print("Kefa")
    else:
        print("Draw")
