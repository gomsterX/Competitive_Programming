#Problem ID: MDL
#Problem Name: Medel

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(min(l), max(l)) if l.index(min(l)) < l.index(max(l))else print(max(l), min(l))
