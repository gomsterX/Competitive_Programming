#Problem ID: SEGM01
#Problem Name: Bear and Segment 01

for _ in range(int(input())):
    s = input()

    b = False
    e = False
    ans = True
    for i in s:
        if i == '1':
            if not e:
                b = True
            else:
                ans = False
                break
        elif i == '0':
            if b and not e:
                e = True
    if(ans and '1' in s):
        print("YES")
    else:
        print("NO")
