#Problem ID: CHEFSQ
#Problem Name: Chef and his Sequence

for _ in range(int(input())):
    n = int(input())
    nl = list(map(int, input().split()))
    m = int(input())
    ml = list(map(int, input().split()))

    c = 0
    for i in nl:
        if (c < m and i==ml[c]):
            c+=1
    if(c == len(ml)):
        print("Yes")
    else:
        print("No")
