#Problem ID: SPELLBOB
#Problem Name: Spell Bob

for _ in range(int(input())):
    s = '' + input() + input()
    boc = 0
    bc = 0
    oc = 0
    for i in range(3):
        if(s[i] == 'b' and s[i+3] == 'o'
                or s[i] == 'o' and s[i+3] == 'b'):
            boc+=1
        elif(s[i] == 'b' or s[i+3] == 'b'):
            bc += 1
        elif(s[i] == 'o' or s[i+3] == 'o'):
            oc += 1
    if(bc >= 2 and oc >= 1
            or boc >= 3 or (boc == 2 and (bc >=1 or oc >= 1))
            or (boc == 1 and (bc == 2 or (bc == 1 and oc == 1)))):
        print("yes")
    else:
        print("no")
