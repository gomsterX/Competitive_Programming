#Problem ID: RNDPAIR
#Problem Name: Random Pair

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = l.count(max(l))
    if c>1:
        print( ((c*(c-1))/2) / ((n*(n-1))/2) )
    else:
        del(l[l.index(max(l))])
        c = l.count(max(l))
        print(c/( (n*(n-1)) /2))
