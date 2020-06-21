#Problem ID: CHEFSTUD
#Problem Name: Chef and his Students

for _ in range(int(input())):
    s = input()
    i = 0
    p = 0
    while i+1 < len(s):
        if(s[i] == '<' and s[i+1] == '>'):
            p += 1
            i+=1
        i+=1

    print(p)
