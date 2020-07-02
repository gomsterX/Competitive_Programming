#Problem ID: CHFCHK
#Problem Name: Chef Chick

for _ in range(int(input())):
    n = input()
    l = list(map(int, input().split()))
    l.sort()
    print(l[0])
