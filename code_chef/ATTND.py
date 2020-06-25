#Problem ID: ATTND
#Problem Name: Attendance

for i in range(int(input())):
    n = int(input())
    l = []
    f = []
    for i in range(n):
        x,y = input().split()
        f.append(x)
        l.append(y)

    for i in range(n):
        if(f.count(f[i]) > 1):
            print(f[i], l[i])
        else:
            print(f[i])

