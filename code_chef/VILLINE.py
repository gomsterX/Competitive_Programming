#Problem ID: VILLINE
#Problem Name: Recruit Villagers

n = int(input())
m, c = map(int, input().split())

p1 = 0
p2 = 0
for i in range(n):
    x, y, p = map(int, input().split())
    Y = m*x +c
    if(y<Y):
        p1 += p
    else:
        p2 += p
print(max(p1, p2))
