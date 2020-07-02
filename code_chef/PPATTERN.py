#Problem ID: PPATTERN
#Problem Name: Print Pattern

for _ in range(int(input())):
    n = int(input())
    l = [0]*n
    for i in range(n):
        l[i] = [0]*n

    c = 1
    ce = n**2
    for i in range(n):
        x=i
        j=0
        while j <= i:
            l[x][j] = c
            j+=1
            x-=1
            c+=1

        if i < n-1:
            x = n - i - 1
            j = n-1
            while x < n:
                l[x][j] = ce
                ce-=1
                j-=1
                x+=1

    for j in range(n):
        for i in range(n):
            print(l[i][j], end=' ')
        print()
