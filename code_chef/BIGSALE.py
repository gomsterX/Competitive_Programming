#Problem ID: BIGSALE
#Problem Name: A Big Sale

for _ in range(int(input())):
    n = int(input())
    s = 0
    for i in range(n):
        p, q, d = map(int, input().split())
        x = p + p*(d/100)
        x = x - x*(d/100)
        s += (p-x)*q
    print(s)
