#Problem ID: ICM2008
#Problem Name: Mr Pr in a Dilemma

for _ in range(int(input())):
    a, b, c, d=map(int, input().split())
    if(a==b):
        print("YES")
    elif(c==d):
        print("NO")


    else:
        if(abs(a-b)%abs(c-d)==0):
            print("YES")
        else:
            print("NO")

