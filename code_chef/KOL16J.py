#Problem ID: KOL16J
#Problem Name: Quentin Tarantin

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = []
    for i in range(1, n+1):
        c.append(i)
    if(l != sorted(l) and sorted(l) == c):
        print("yes")
    else:
        print("no")
