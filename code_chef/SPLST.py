#Problem ID: SPLST
#Problem Name: Split Stones

for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    if a+b+c == x+y and min(x, y)>=min(a, b, c):
        print('YES')
    else:
        print('NO')
