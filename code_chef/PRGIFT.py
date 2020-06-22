#Problem ID: PRGIFT
#Problem Name: Chef and Gift

for _ in range(int(input())):
    n, ev = map(int, input().split())
    l = list(map(int, input().split()))

    c = 0
    g = False
    for i in range(n):
        if l[i] % 2 == 0:
            c += 1
    if(ev==0):
        print("NO")
    elif(c >= ev):
        print("YES")
    else:
        print("NO")
