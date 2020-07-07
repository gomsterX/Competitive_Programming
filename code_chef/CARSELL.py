#Problem ID: CARSELL
#Problem Name: Sell All the Cars

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l = list(filter(lambda x: x!=0, l))
    l.sort(reverse = True)
    if(len(l) > 1):
        for i in range(n):
            l[i] -= i
            if l[i] < 0:
                l[i] = 0
    print(sum(l)%1000000007)

