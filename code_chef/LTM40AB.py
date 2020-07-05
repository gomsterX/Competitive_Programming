#Problem ID: LTM40AB
#Problem Name: Chef and Inequality

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    t = 0
    for i in range(a, b+1):
        if(i<c):
            t+=d-c+1
        elif i < d:
            t+= d-i
    print(t)
