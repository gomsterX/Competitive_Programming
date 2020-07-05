#Problem ID: EID2
#Problem Name: Eidi Gift

for _ in range(int(input())):
    l = list(map(int, input().split()))
    x = l[3:]
    l = l[:3]
    fr = True
    for i in range(3):
        c = i+1
        if c > 2:
            c%=3
        if((x[i] == x[c] and l[i] != l[c])
                or(x[i] > x[c] and l[i] <= l[c])
                or(x[i] < x[c] and l[i] >= l[c])):
            fr = False
            break
    if(fr):
        print("FAIR")
    else:
        print("NOT FAIR")
