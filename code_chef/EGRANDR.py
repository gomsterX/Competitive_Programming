#Problem ID: EGRANDR
#Problem Name: Andrash and Stipendium

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in l:
        if i <= 2:
            s = 0
            break
        else:
            s+=i
    if(s/n >= 4 and 5 in l):
        print("Yes")
    else:
        print("No")
