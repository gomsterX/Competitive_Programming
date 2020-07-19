#Problem ID: TRACE
#Problem Name: Trace of Matrix

for _ in range(int(input())):
    n = int(input())
    l = []
    mx = 0
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(n):
        s1 = 0
        s2 = 0
        x = i
        y = 0
        while x < n and y < n:
            s1 += l[y][x]
            s2 += l[x][y]
            x +=1
            y +=1
        mx = max(mx, s1, s2)
    print(mx)
