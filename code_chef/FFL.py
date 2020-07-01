#Problem ID: FFL
#Problem Name: Chef in Fantasy League

for _ in range(int(input())):
    n, s = map(int, input().split())
    p = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    x, y = 100000, 100000

    for i in range(n):
        if pos[i] == 0 and p[i] < x:
            x = p[i]
        elif pos[i] == 1 and p[i] < y:
            y = p[i]
    if x+y+s <= 100:
        print("yes")
    else:
        print("no")
