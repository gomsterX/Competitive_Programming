#Problem ID: CHFM
#Problem Name: Chef and Mean

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = sum(l)
    min_coin = 0
    ind = 0
    for i in range(n):
        if(x/n == (x-l[i])/(n-1)):
            if(min_coin == 0) or l[i] < min_coin:
                min_coin = l[i]
                ind = i+1
    if(min_coin == 0):
        print("Impossible")
    else:
        print(ind)
