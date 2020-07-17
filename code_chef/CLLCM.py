#Problem ID: CLLCM
#Problem Name: Chef vs Doof

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    p = True
    for i in l:
        if i % 2 == 0:
            p = False
            break
    if p:
        print('YES')
    else:
        print('NO')
