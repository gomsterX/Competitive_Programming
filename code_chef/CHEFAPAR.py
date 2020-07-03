#Problem ID: CHEFAPAR
#Problem Name: Chef and His Apartment Dues

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if(l.count(0) > 0):
        x = l.index(0)
        print(l[x:].count(0) * 1000 + len(l[x:])*100)
    else:
        print(0)
