#Problem ID: NAICHEF
#Problem Name: Naive Chef

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    l = list(map(int, input().split()))
    a, b = l.count(a), l.count(b)
    print(a*b/(n**2))
