#Problem ID: REACTION
#Problem Name: Chain Reaction

for _ in range(int(input())):
    n, k = map(int, input().split())
    l=[]
    stable = True

    for i in range(n):
        l.append(list(map(int, input().split())))

    for i in range(n):
        x = 0
        x = 1 if i == 0 or i == n-1 else 2
        m = x
        for j in range(k):
            x = m
            x = x + 1 if j == 0 or j == k-1 else x+2
            if l[i][j] >= x:
                stable = False
                break
    if stable:
        print("Stable")
    else:
        print("Unstable")
