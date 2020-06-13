#Problem ID: FRGTNLNG
#Problem Name: Forgotten Language

for _ in range(int(input())):
    n, k = map(int, input().split())
    n = list(input().split())
    x = [''] * k

    for i in range(k):
        x[i] = list(input().split())

    x = sum(x, [])

    for word in n:
        if word in x:
            print("YES ", end = '')
        else:
            print("NO ", end = '')
