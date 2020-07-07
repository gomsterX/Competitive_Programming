#problem: /contest/1371/problem/D
#problem Name: D. Grid-00100

for _ in range(int(input())):
    n,k = map(int, input().split())
    l = [[1]*n for i in range(n)]
    if(n**2 > k):
        k = n**2-k

        i = j = 0
        c= 1
        m = 0
        while(k!=0):
            if(m == n):
                i = (i+c) %n
                m = 0
            if i == n:
                i = i%n
            if(j == n):
                j = 0
            l[j][i] = 0
            k-=1
            i+=1
            m+=1
            j+=1
    mxr = mnr = sum(l[0])
    mxc = mnc = sum([l[i][0] for i in range(n)])
    for i in range(n):
        s = sum(l[i])
        mxr = max(s, mxr)
        mnr = min(s, mnr)
        s = sum([l[j][i] for j in range(n)])
        mnc = min(s, mnc)
        mxc = max(s, mxc)
    print((mxr-mnr)**2+(mxc-mnc)**2)
    for i in range(n):
        print(*l[i], sep='')


