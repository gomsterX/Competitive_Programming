#Problem ID: RECNDNOS
#Problem Name: Chef and Numbers

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    while i+1 < len(l):
        if l[i] == l[i+1]:
            del(l[i+1])
        i+=1
    x = list(set(l))
    x.sort()
    c , d = 0, 0
    for i in x:
        if l.count(i)>c:
            c = l.count(i)
            d = i
    print(d)
