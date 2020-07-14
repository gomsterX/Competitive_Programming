#Problem ID: KOL15A
#Problem Name: Processing a string

for _ in range(int(input())):
    x = input()
    c = 0
    for i in x:
        if i.isdigit():
            c+=int(i)
    print(c)
