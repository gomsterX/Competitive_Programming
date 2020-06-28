#Problem ID: JDELAY
#Problem Name: Judging Delay

for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in range(n):
        x, y = map(int, input().split())
        if(y-x >5):
            c+=1
    print(c)
