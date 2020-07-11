#Problem ID: MGCSET
#Problem Name: Magic Set

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    c=0
    for i in range(n):
        if l[i] %m == 0:
            c+=1
    print(2**c - 1)
