#Problem ID: ORDTEAMS
#Problem Name: Ordering teams

for _ in range(int(input())):
    c = True
    s = [list(map(int, input().split())) for i in range(3)]
    s.sort()
    if(sum(s[0]) >= sum(s[1]) or sum(s[1]) >= sum(s[2])):
        c = False
    else:
        if(s[0][0] > s[1][0] or s[1][0] > s[2][0]
                or s[0][1] > s[1][1] or s[1][1] > s[2][1]):
            c = False

    if c :
        print('yes')
    else:
        print('no')

