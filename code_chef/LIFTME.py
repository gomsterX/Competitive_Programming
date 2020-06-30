#Problem ID: LIFTME
#Problem Name: Lift Requests

for _ in range(int(input())):
    n, q = map(int, input().split())
    x = 0
    t = 0
    for i in range(q):
        a, b = map(int, input().split())
        t += abs(x-a) + abs(b-a)
        x=b
    print(t)
