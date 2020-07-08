#Problem ID: TRUEDARE
#Problem Name: Truth and Dare

for _ in range(int(input())):
    tr = int(input())
    Tr = list(map(int, input().split()))
    dr = int(input())
    Dr = list(map(int, input().split()))
    ts = int(input())
    Ts = list(map(int, input().split()))
    ds = int(input())
    Ds = list(map(int, input().split()))
    t = True
    for i in Ts:
        if i not in Tr:
            t = False
            break
    if t:
        for i in Ds:
            if i not in Dr:
                t = False
                break
    if t:
        print('yes')
    else:
        print('no')
