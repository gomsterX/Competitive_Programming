#Problem ID: PLAYPIAN
#Problem Name: Play Piano

for _ in range(int(input())):
    t = True
    d = input()
    n = len(d)

    if(n%2 != 0):
        t = False
    else:
        i = 0
        while(i < n):
            if((d[i] == 'A' and d[i+1] == 'B')
                    or (d[i] == 'B' and d[i+1] == 'A')):
                i+=2
            else:
                t = False
                break
    if(t):
        print("yes")
    else:
        print("no")

