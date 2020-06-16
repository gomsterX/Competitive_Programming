#Problem ID: VCS
#Problem Name: Version Control System

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    f = [[False, False] for i in range(n)]
    ignrd = list(map(int, input().split()))
    trckd = list(map(int, input().split()))

    for i in range(m):
        f[ignrd[i] - 1][0] = True
    for i in range(k):
        f[trckd[i] - 1][1] = True

    x = 0
    y = 0
    for i in range(n):
        if(f[i][0] == True and f[i][1] == True):
            x += 1
        elif(f[i][0] == False and f[i][1] == False):
            y += 1
    print(x, y)
