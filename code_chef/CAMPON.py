#Problem ID: CAMPON
#Problem Name: Camp Or Not

for _ in range(int(input())):
    d = [0]*31
    for i in range(int(input())):
        n, k = map(int, input().split())
        d[n-1] += k
    for i in range(int(input())):
        x, y = map(int, input().split())
        if sum(d[:x]) >= y:
            print("Go Camp")
        else:
            print("Go Sleep")

