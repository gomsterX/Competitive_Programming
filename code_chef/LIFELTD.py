#Problem ID: LIFELTD
#Problem Name: Life Limited

for _ in range(int(input())):
    l = []
    good = False
    for i in range(3):
        l.append(input())
    for i in range(2):
        for j in range(2):
            if(l[i][j] == 'l'):
                if(l[i+1][j] == 'l'):
                    if(l[i+1][j+1] == 'l'):
                        good = True
    if(good):
        print("yes")
    else:
        print("no")
