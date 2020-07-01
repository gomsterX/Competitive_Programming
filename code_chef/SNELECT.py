#Problem ID: SNELECT
#Problem Name: Snakes, Mongooses and the Ultimate Election

for _ in range(int(input())):
    s = list(input())

    i = 0
    while i < len(s)-1:
        if s[i] != s[i+1]:
            if s[i] == 's':
                del(s[i])
            else:
                del(s[i+1])
        i+=1

    snakes = s.count('s')
    mon = s.count('m')
    if(snakes > mon):
        print("snakes")
    elif(snakes < mon):
        print("mongooses")
    else:
        print("tie")

