#Contest Name: Codeforces Round #653 (Div. 3)
#Problem Name: B) Multiply by 2, Divide by 6

for _ in range(int(input())):
    x = int(input())
    c=0

    while(x != 1):
        if(x%2 == 0 and x%6 != 0):
            c = -1
            break
        elif(x%6 == 0):
            x//=6
            c+=1
        else:
            x*=2
            c+=1

    print(c)
