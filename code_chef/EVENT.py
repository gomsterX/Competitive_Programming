#Problem ID: EVENT
#Problem Name: Event
x = {'sat':1, 'sun':2, 'mon':3, 'tue':4, 'wed':5, 'thu':6, 'fri':7}

for _ in range(int(input())):
    s, e, l, r = input().split()
    l, r = int(l), int(r)
    s, e = x[s[:3]], x[e[:3]]

    ds = 1
    if s < e:
        ds += e-s
    elif s > e:
        ds += (7-s)+e

    t = 0
    count = 0
    while (ds <= r):
        if ds >= l and ds <= r:
            count += 1
            t = ds
        ds += 7
    if count >0:
        print(t) if count == 1 else print('many')
    else:
        print('impossible')

