#Problem ID: SNAKPROC
#Problem Name: Snake Procession

for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    for i in range(n):
        if c < 0 or c > 1:
            break
        elif s[i] == 'H':
            c+=1
        elif s[i] == 'T':
            c-=1
    if(c==0):
        print("Valid")
    else:
        print("Invalid")
