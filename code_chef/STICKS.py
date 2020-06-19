#Problem ID: STICKS
#Problem Name: Sticks

for _ in range(int(input())):
    n = int(input())
    x = sorted(list(map(int, input().split())), reverse = True)
    d = []

    i = 0
    while(i < n - 1):
        if(x[i] == x[i+1]):
            d.append(x[i])
            i += 2
        else:
            i+=1
    if(len(d) <=1 ):
        print(-1)
    else:
        print(d[0] * d[1])
