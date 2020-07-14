#Problem ID: EVENT
#Problem Name: Event

x = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
for _ in range(int(input())):
    s, e, l, r = input().split()
    s = x.index(s)+1
    e = x.index(e)+1
    l, r = int(l), int(r)
    c = 0
    if s>e:
        c += (7-s+1)+e
    else:
        c += (e-s+1)
    if c >= l and r <= 7:
        print(c)
    elif c >= l:
        print('many')
    else:
        print('impossible')
