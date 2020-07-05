#Problem ID: VALIDSTK
#Problem Name: Valid Stack Operations

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    psh = 0
    pp = 0

    stk = True
    for i in l:
        if i == 1:
            psh += 1
        else:
            pp += 1
        if pp > psh:
            stk = False
    if stk:
        print("Valid")
    else:
        print("Invalid")
