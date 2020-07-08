#Problem ID: COVID19
#Problem Name: Coronavirus Spread

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    m = []
    x = []
    i = 0
    while i < n:
        x.append(l[i])
        if i+1 == n:
            m.append(x)
            break
        if(abs(l[i]-l[i+1]) >= 3):
            m.append(x)
            x = []
        i+=1
    min_inf, max_inf = min([len(m[i]) for i in range(len(m))]), max([len(m[i]) for i in range(len(m))])
    print(min_inf, max_inf)



