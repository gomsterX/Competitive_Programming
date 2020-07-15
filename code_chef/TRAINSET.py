#Problem ID: TRAINSET
#Problem Name: Select Training Set

for _ in range(int(input())):
    l = dict()
    for i in range(int(input())):
        m , n = input().split()
        n = int(n)
        if m in l:
            l[m][n]+=1
        else:
            l[m] = [0, 0]
            l[m][n]+=1
    c=0
    for i in l:
        c+= max(l[i])
    print(c)
