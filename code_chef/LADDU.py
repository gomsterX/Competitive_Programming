#Problem ID: LADDU
#Problem Name: Laddu

act = {"TOP_CONTRIBUTOR": 300, "CONTEST_HOSTED": 50}
for _ in range(int(input())):
    n, k = input().split()
    n = int(n)
    pnts = 0
    for i in range(n):
        x = input()
        if x not in act:
            x, y = x.split()
            y = int(y)
            if(x == 'BUG_FOUND'):
                pnts += y
            else:
                pnts = pnts + 300 + 20-y if y < 20 else pnts + 300
        else:
            pnts += act[x]
    if k == 'INDIAN':
        print(int(pnts/200))
    else:
        print(int(pnts/400))
