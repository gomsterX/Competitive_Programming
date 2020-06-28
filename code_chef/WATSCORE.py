#Problem ID: WATSCORE
#Problem Name: That Is My Score!

for _ in range(int(input())):
    n = int(input())
    p = [0] * 12

    for i in range(n):
        x, y = list(map(int, input().split()))
        p[x] = max(p[x], y)

    print(sum(p[0:9]))
