#Problem ID: CHEGLOVE
#Problem Name: Chef and Glove

for _ in range(int(input())):
    n = int(input())
    f = list(map(int, input().split()))
    s = list(map(int, input().split()))

    front = True
    back = True

    for i in range(n):
        if(f[i] > s[i]):
            front = False
        if(f[i] > s[n - i - 1]):
            back = False

    if front and back:
        print("both")
    elif front:
        print("front")
    elif back:
        print("back")
    else:
        print("none")
