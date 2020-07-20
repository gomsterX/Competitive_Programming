#Problem ID: GIT01
#Problem Name: Chef And his Cake

for _ in range(int(input())):
    n, m = map(int, input().split())
    c1 = c2 = 0
    x = 'RG' * m
    y = 'GR' * m
    if m%2:
        x, y = x[:-1], y[:-1]
    for i in range(n):
        l = input()
        if i % 2 == 0:
            for i in range(m):
                if l[i] != x[i]:
                    c1 = c1 + 5 if l[i] == 'R' else c1 + 3
                if l[i] != y[i]:
                    c2 = c2 + 5 if l[i] == 'R' else c2 + 3
        else:
            for i in range(m):
                if l[i] != y[i]:
                    c1 = c1 + 5 if l[i] == 'R' else c1 + 3
                if l[i] != x[i]:
                    c2 = c2 + 5 if l[i] == 'R' else c2 + 3
    print(min(c1, c2))
