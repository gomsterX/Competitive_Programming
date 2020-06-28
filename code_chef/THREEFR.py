#Problem ID: THREEFR
#Problem Name: Three Friends

for _ in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    if(l[2] - l[0] - l[1]):
        print("no")
    else:
        print("yes")
