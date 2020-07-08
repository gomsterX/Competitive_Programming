#Problem ID: MXCH
#Problem Name: Dinosaurs Football

for _ in range(int(input())):
    n, k = map(int, input().split())
    i = 0
    c = 1
    while i<n:
        if i == k:
            print(n, end = ' ')
        else:
            print(c, end = ' ')
            c+=1
        i+=1
    print()
