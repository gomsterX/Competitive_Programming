#Problem ID: NITIKA
#Problem Name: Whats in the Name

for _ in range(int(input())):
    s = list(input().split())
    x = len(s)
    for i in range(len(s)):
        if i < len(s)-1:
            s[i] = s[i][0].upper()+'. '
        else:
            s[i] = s[i].lower()
            s[i] = s[i][0].upper() + s[i][1:]
    for i in s:
        print(i, end = '')
    print()
