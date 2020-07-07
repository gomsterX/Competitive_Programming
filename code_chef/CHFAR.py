#Problem ID: CHFAR
#Problem Name: Chef and Sequence

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if(n - l.count(1) <= k):
        print('YES')
    else:
        print('NO')

