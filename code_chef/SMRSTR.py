#Problem ID: SMRSTR
#Problem Name: Smart Strategy

for _ in range(int(input())):
    n, q = map(int, input().split())
    d = list(map(int, input().split()))
    x = list(map(int, input().split()))
    p = 1
    for i in d:
        p=p*i
    for i in x:
        print(i//p, end = ' ')
    print()
