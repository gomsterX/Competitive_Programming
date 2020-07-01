#Problem ID: PCJ18A
#Problem Name: Chef and Secret Ingredient

for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))

    liked = False
    for i in l:
        if i>=x:
            liked = True
            break
    if liked:
        print("YES")
    else:
        print("NO")
