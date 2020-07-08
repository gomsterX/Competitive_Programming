#Problem ID: CHNUM
#Problem Name: Chef and Number Game

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    pos = neg = 0
    for i in l:
        if i > 0:
            pos += 1
        else:
            neg +=1
    if pos == n or neg == n:
        print(n, n)
    else:
        print(max(pos, neg), min(pos, neg))
