#Problem ID: MATCHES
#Problem Name: Playing with Matches

for _ in range(int(input())):
    x, y = map(int, input().split())
    x += y
    x = list(str(x))
    matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    c = 0
    for i in x:
        c += matches[int(i)]
    print(c)
