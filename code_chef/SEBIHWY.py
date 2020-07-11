#Problem ID: SEBIHWY
#Problem Name: Sebi and the highway

for _ in range(int(input())):
    s, sg, fg, d, t = map(int, input().split())
    x = (180*d/t)+s
    if(abs(x-sg) > abs(x-fg) ):
        print("FATHER")
    elif (abs(x-sg)<abs(x-fg)):
        print("SEBI")
    else:
        print("DRAW")

