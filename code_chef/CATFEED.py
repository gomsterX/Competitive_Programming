#Problem ID: CATFEED
#Problem Name: Chef Feeds Cats

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    fair = True
    if(m<n):
        if(len(set(l))<m):
            fair = False
    else:
        for i in range(0, m, n):
            if(i+n > m and len(set(l[i:])) < len(l[i:])):
                fair = False
            if(i+n <= m and len(set(l[i:i+n])) < n):
                fair = False
    if fair:
        print("YES")
    else:
        print("NO")

