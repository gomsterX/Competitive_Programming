#Problem ID: NUMCOMP
#Problem Name: Archi and Comparsion

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    if a<0 and n%2 == 0:
        a *=(-1)
    if b<0 and n%2 == 0:
        b *=-1
    if a>b:
        print(1)
    elif b>a:
        print(2)
    else:
        print(0)
