#Problem ID: NOTINCOM
#Problem Name: Nothing in Common

for _ in range(int(input())):
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = set(a+b)

    print(x+y - len(l))
