

for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    x = 0
    for i in range(n):
        if(s[i] == '('):
            if(x < 0):
                c += abs(x)
                x = 0
            x +=1
        elif(s[i] == ')'):
            x -= 1
    print(c)
