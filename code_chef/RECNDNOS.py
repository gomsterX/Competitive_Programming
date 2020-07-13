#Problem ID: RECNDNOS
#Problem Name: Chef and Numbers

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    i = 1
    while i < len(l):
        if l[i] == l[i-1]:
            del l[i-1]
            i+=1
        i+=1
    x = list(set(l))
    x.sort()
    mx = 0
    d = None
    for i in x:
        if l.count(i) > mx:
            mx = l.count(i)
            d = i
            print(i, l.count(i))
    print(d)
