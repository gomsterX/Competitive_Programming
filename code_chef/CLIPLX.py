#Problem ID: CLIPLX
#Problem Name: IPL and RCB

for _ in range(int(input())):
    x, y = map(int, input().split())

    n=0
    if(x<=y):
        n = 0
    else:
        n = x-y
    print(n)
