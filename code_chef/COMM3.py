#Problem ID: COMM3
#Problem Name: Three Way Communication

import math

for _ in range(int(input())):
    r = int(input())

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    d1 = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
    d2 = (math.sqrt((x2 - x3)**2 + (y2 - y3)**2))
    d3 = (math.sqrt((x3 - x1)**2 + (y3 - y1)**2))
    count = 0
    if(d1 <= r):
        count +=1
    if(d2 <= r):
        count +=1
    if(d3 <= r):
        count +=1
    if(count >= 2):
        print("yes")
    else:
        print("no")
