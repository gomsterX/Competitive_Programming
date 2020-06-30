#Problem ID: CHNGIT
#Problem Name: Change It

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    mx = 0
    for i in l:
        mx = max(mx, l.count(i))

    print(len(l) - mx)
