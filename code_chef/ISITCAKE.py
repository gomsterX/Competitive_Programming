#Problem ID: ISITCAKE
#Problem Name: Is it a Cakewalk Problem

for _ in range(int(input())):
    x=[]
    c = 0

    for i in range(10):
        x+=list(map(int, input().split()))
    for i in x:
        if i <= 30:
            c+=1
    if(c >= 60):
        print("yes")
    else:
        print("no")
