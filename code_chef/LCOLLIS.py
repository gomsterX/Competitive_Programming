#Problem ID: LCOLLIS
#Problem Name: Collisions

for _ in range(int(input())):
    n, m = map(int, input().split())
    l=[]
    for i in range(m):
        l.append('')
    for i in range(n):
        s = input()
        for j in range(m):
            l[j] += s[j]

    col = 0
    for i in l:
        x = i.count('1')
        col += x*(x-1)/2
    print(int(col))

