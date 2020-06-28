#Problem ID: ENCMSG
#Problem Name: Encoding Message

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    i = 0
    while(i < n):
        if(i+1 >= n):
            break
        s[i], s[i+1] = s[i+1], s[i]
        i += 2

    for i in range(n):
        s[i] = chr(123 - (ord(s[i])+26)%122)

    for i in s:
        print(i, end='')
    print()
