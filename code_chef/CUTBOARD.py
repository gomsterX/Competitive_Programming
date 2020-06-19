#Problem ID: CUTBOARD
#Problem Name: Cut the Board

for _ in range(int(input())):
    x, y = map(int, input().split())
    print((x-1) * (y-1))
