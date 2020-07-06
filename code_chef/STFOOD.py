#Problem ID: STFOOD
#Problem Name: Chef and Street Food

for _ in range(int(input())):
    n = int(input())
    prof = 0
    for i in range(n):
        s, p, v = map(int, input().split())
        prof = max(p//(s+1) * v, prof)
    print(int(prof))
