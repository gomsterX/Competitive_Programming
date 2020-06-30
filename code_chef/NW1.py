#Problem ID: NW1
#Problem Name: Days in Month

d = ["mon", "tues", "wed","thurs", "fri", "sat", "sun"]
for _ in range(int(input())):
    n, x = input().split()
    dd = int(n)
    n, x = int(n), d.index(x)

    l = [0]*7
    for i in range(x, x+n):
        i%=7
        l[i]+=1


    for i in l:
        print(i, end=' ')
    print()


