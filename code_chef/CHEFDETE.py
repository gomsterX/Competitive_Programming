#Problem ID: CHEFDETE
#Problem Name: Chef-Detective

n = int(input())
l = list(map(int, input().split()))
l.sort()
r = [True] * n
for i in l[1:]:
    r[i-1] = False
for i in range(n):
    if r[i]:
        print(i+1, end = ' ')
print()
