#Problem ID: CHEFRECP
#Problem Name: Chef and Recipe

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = []
    x=[]
    chef = True
    for i in range(n):
        if i == n-1 or l[i] != l[i+1]:
            if l[i] in m:
                chef = False
                break
            if l.count(l[i]) in x:
                chef = False
                break
            m.append(l[i])
            x.append(l.count(l[i]))
    if chef:
        print('YES')
    else:
        print('NO')

