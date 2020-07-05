#Problem ID: EXUNA
#Problem Name: Weird Modulo Problem

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    c = l[0]
    for i in range(1, n):
        c %= l[i]

    print(c)
