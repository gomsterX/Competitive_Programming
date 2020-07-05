#Problem ID: UWCOI20A
#Problem Name: Peak Finding

for _ in range(int(input())):
    x = 0
    for i in range(int(input())):
        n = int(input())
        if(n > x):
            x = n
    print(x)
