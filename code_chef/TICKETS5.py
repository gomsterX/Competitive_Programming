#Problem ID: TICKETS5
#Problem Name: Tickets

for _ in range(int(input())):
    s = input()
    c = len(s) - 1
    j = [s[0], s[1]]

    for i in range(len(s) - 1):
        if(s[i] != s[i+1] and (s[i] and s[i+1] in j)):
            c-=1
        else:
            break
    if c== 0:
        print("YES")
    else:
        print("NO")
