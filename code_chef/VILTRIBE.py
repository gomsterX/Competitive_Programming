#Problem ID: VILTRIBE
#Problem Name: Villages and Tribes

for _ in range(int(input())):
    s = input()
    i = 0
    a = b = 0
    while i < len(s):
        if(s[i] == 'A'):
            a +=1
            x = 0
            i+=1
            while i < len(s):

                if(s[i] == 'B'):
                    i-=1
                    break
                elif s[i] == 'A':
                    a += x+1
                    x = 0
                else:
                    x += 1
                i+=1
        elif s[i] == 'B':
            b+=1
            x = 0
            i+=1
            while i < len(s):
                if(s[i] == 'A'):
                    i-=1
                    break
                elif s[i] == 'B':
                    b += x+1
                    x = 0
                else:
                    x +=1
                i+=1


        i+=1
    print(a, b)
