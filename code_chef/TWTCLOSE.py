#Problem ID: TWTCLOSE
#Problem Name: Closing the Tweets

n, k = map(int, input().split())
twts = [0] * n

for _ in range(k):
    x, *y = input().split()
    y = (int(y[0])-1) if y else ' '
    if(x == "CLOSEALL"):
        twts = [0]*n
    else:
        twts[y] = not twts[y]
    print(sum(twts))
