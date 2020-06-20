#Problem ID: TABLET
#Problem Name: Buying New Tablet

for _ in range(int(input())):
    bought_area = 0
    n, p = map(int, input().split())
    for i in range(n):
        x, y, z = map(int, input().split())
        if(z <= p and (x*y) > bought_area):
            bought_area = x*y

    print(bought_area) if bought_area else print("no tablet")


