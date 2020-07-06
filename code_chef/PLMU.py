#Problem ID: PLMU
#Problem Name: Plus Multiply

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x, y = l.count(2), l.count(0)
    if(x > 1 or y > 1):
        print( int((x * (x-1)) / 2) + int((y * (y-1)) / 2))
    else:
        print(0)
