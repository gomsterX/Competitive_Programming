#Problem ID: POPGATES
#Problem Name: At the Gates

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(input().split())
    if(l[n-k] == 'T'):
        print(l[:n-k].count('H'))
    else:
        print(l[:n-k].count('T'))
